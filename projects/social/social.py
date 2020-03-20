from random import shuffle, choice
from util import Queue

# Contains almost 5k names
with open('friends.txt') as friends_list:
    friends = [line.strip() for line in friends_list]

# 
short_friends_list = []
shuffle(friends)
for i in range(len(friends)):
    if i < 1000:
        short_friends_list.append(friends[i])
# print(short_friends_list)
    
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        if friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[name] = User(name)
        self.friendships[name] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        # self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for name in short_friends_list:
            self.add_user(name)

        # Create a list of all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in short_friends_list:
                # possible_friendships.append(friend_id)
                if user_id is not friend_id:
                    friends = (user_id, friend_id)
                    possible_friendships.append(friends)

        # Next, we shuffle the list of possible friendships
        shuffle(possible_friendships)

        # Grab the first N pairs from the shuffled list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            count = i
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            count += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Create an empty queue
        queue = Queue()
        # Create a path
        path = []
        # Create a visited dic
        visited = {}
        # Add the initial vertex to the path
        path.append(user_id)
        # Then add the path to the queue, should be initialized as a empty list
        queue.enqueue(path)
        # we initialize the dictionary with the user id
        visited[user_id] = path
        # counter that tracks how many times we traversed over our graph
        counter = 0
        # Prints all users and their friends
        for i in self.friendships:
            print(i, 'friends:', self.friendships[i])

        # While the queue is not empty...
        while queue.size() > 0:
            # We dequeue the path
            path = queue.dequeue()
            # We grab the last vertex in the path
            last_vertex = path[-1]
            # check if it has NOT been visited...
            if last_vertex not in visited:
                # If not, we add it to the visited dic
                # we initialized a boolean here to check if the last vertex is a friend of the user id
                friends = False
                # so we traverse over the user id friends...
                # for friends_id in self.friendships[user_id]:
                    # if the last vertex is found, it means they are friends..
                if last_vertex in self.friendships[user_id]:
                    # so we turn the boolean to True
                    friends = True
                    # and we set in the dictionary the connection
                    visited[last_vertex] = [user_id, last_vertex]
                # this variable will hold all the mutual friends of the current vertex and the user id
                mutual_friends = []
                # at this point we check if the last vertex is not a friend of the user id by checking the friends boolean..
                if friends is False:
                    # so we check if they both share a mutual connection in their list of friends..
                    for mutual_friend in self.friendships[last_vertex]:
                        for connection in self.friendships[user_id]:
                            # if they do we add the user id, last vertex and their mutual connections
                            if mutual_friend is connection:
                                mutual_friends.append(mutual_friend)
                # we check if there is any mutual friends..
                if (bool(mutual_friends)) is True:
                    # If there is, we iterate over them and add them to the friends list
                    visited[last_vertex] = [last_vertex, user_id]
                    for mutual_friend in mutual_friends:
                        visited[last_vertex].insert(1, mutual_friend)
            # ---------------------------------- RETURNS THE EXTENDED NETWORK LIST
            counter += 1
            if counter == len(self.friendships):
                # if so, we return visited
                print('visited', visited)
                return visited
            # we traverse over the friendships dic...
            for friend in self.friendships:
                # we check if the neighbor is NOT marked as visited...
                if friend not in visited:
                    # if it is not, we make a copy of the path
                    path_copy = path.copy()
                    # we append the friend to the copy of the path
                    path_copy.append(friend)
                    # then we add the copy of the path to the queue
                    queue.enqueue(path_copy)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(len(short_friends_list), 5)
    users = choice([user for user in sg.users.keys()])
    sg.get_all_social_paths(users)

    # connections = sg.get_all_social_paths(users)
    # print(len(connections) / 1000)

    # total = 0
    # for path in connections.values():
    #     total += len(path)
    # print(f'Avg length = {total / len(connections) - 1}')
