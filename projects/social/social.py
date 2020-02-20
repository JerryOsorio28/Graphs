from random import shuffle
from util import Queue

# Contains almost 5k names
with open('friends.txt') as friends_list:
    friends = [line.strip() for line in friends_list]

# 
short_friends_list = []
for i in range(len(friends)):
    if i <= 5:
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
            print('WORKING')
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
        # print('num of users', num_users)
        # for i in range(1, num_users + 1):
        #     self.add_user(f'User {i}')
        for name in short_friends_list:
            self.add_user(name)

        # Create a list of all possible friendships
        possible_friendships = []
        for user_id in self.users:
            # print('user_id', user_id)
            for friend_id in short_friends_list:
                # possible_friendships.append(friend_id)
                if user_id is not friend_id:
                    friends = (user_id, friend_id)
                    possible_friendships.append(friends)

                    
        print('possible_friendships', possible_friendships)
        # print('nono_repeat',no_repeat)
        # print('users', self.users)

        # Next, we shuffle the list of possible friendships
        shuffle(possible_friendships)
        # print('possible_friendships', possible_friendships)

        # Grab the first N pairs from the shuffled list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            # print('friendship', friendship)
            self.add_friendship(friendship[0], friendship[1])

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
        
        print('self.friendships', self.friendships)
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
                for friends_id in self.friendships[user_id]:
                    # if the last vertex is found, it means they are friends..
                    if last_vertex is friends_id:
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
                            if mutual_friend is connection:
                                mutual_friends.append(mutual_friend)
                    # if they do we add the user id, last vertex and their mutual connections
                    print('mutual friends', last_vertex, mutual_friends)
                # we check if there is any mutual friends..
                if (bool(mutual_friends)) is True:
                    # If there is, we iterate over them and add them to the friends list
                    for mutual_friend in mutual_friends:
                        visited[last_vertex] = [user_id, last_vertex]
                        visited[last_vertex].insert(1, mutual_friend)
            # we check if the last vertex is the last id in friendships (it reached the end of the friendships dic)
            if last_vertex == len(self.friendships):
                # print('visited',visited)
                # if so, we return visited
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
    sg.populate_graph(len(short_friends_list), 2)
    # sg.add_user('Aaren')
    # sg.add_friendship(1, 2)
    # sg.get_all_social_paths(2)
    print(sg.friendships)
    # print('User`s Graph', sg.users)
    # connections = sg.get_all_social_paths(1)
    # print(connections)