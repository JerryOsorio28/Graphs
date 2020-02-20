from random import shuffle
from util import Queue

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
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # print('num of users', num_users)
        for i in range(1, num_users + 1):
            self.add_user(f'User {i}')

        # Create a list of all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Next, we shuffle the list of possible friendships
        shuffle(possible_friendships)
        # print('possible_friendships', possible_friendships)

        # Grab the first N pairs from the shuffled list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
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

        visited[user_id] = path
        # print('visited', visited)

        print('self.friendships.values', self.friendships)
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue, the first PATH
            path = queue.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            last_vertex = path[-1]
            # print('last_vertex', last_vertex)
            # check if it has NOT been visited...
            if last_vertex not in visited:
                # If not, we add it to the visited dic
                friends = False
                for friends_id in self.friendships[user_id]:
                    if last_vertex is friends_id:
                        friends = True
                        visited[last_vertex] = [user_id, last_vertex]
                if friends is False:
                    for mutual_friend in self.friendships[last_vertex]:
                        for connection in self.friendships[user_id]:
                            if mutual_friend is connection:
                                visited[last_vertex] = [user_id, mutual_friend, last_vertex]
            if last_vertex == len(self.friendships):
                print('visited',visited)
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
    sg.populate_graph(10, 2)
    sg.add_friendship(1, 2)
    # print('friendships', sg.friendships)
    sg.get_all_social_paths(1)
    # print('User`s Graph', sg.users)
    # connections = sg.get_all_social_paths(1)
    # print(connections)


    # 
