from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def bread_first_traversal(my_rooms_graph):
    # Player's current room ID
    room_id = player.current_room.id
    # Queue
    q = Queue()
    # We add to our queue our current room's ID
    q.enqueue([room_id])
    # Keeps a track of our visited rooms
    visited = set()

    while q.size() > 0:
        # We remove our path from our queue
        path = q.dequeue()
        # and we gran the last value of it
        last_room = path[-1]
        # we check if the last room is not marked as visited
        if last_room not in visited:
            # if it's not we mark it as visited
            visited.add(last_room)
            # we check the exits of the last room in our path
            for next_exit in my_rooms_graph[last_room]:
                # if any of the next_exit have a '?' mark..
                if my_rooms_graph[last_room][next_exit] == '?':
                    # we return the path
                    return path
                # else we check if the next exit is in visited..
                elif my_rooms_graph[last_room][next_exit] not in visited:
                    # if it is not, we make a copy of the path
                    path_copy = path.copy()
                    # we append the next exit to the copy of the path
                    path_copy.append(my_rooms_graph[last_room][next_exit])
                    # then we add the copy of the path to the queue
                    q.enqueue(path_copy)


def traverse_world():
    # If the player has reached to an already explored room, this method returns the opposite direction, making possible to tap into the next room's cardinal point and update it
    # with the player's current room ID.
    def opposite_direction(direction):
        if direction == 'n':
            return 's'
        elif direction == 's':
            return 'n'
        elif direction == 'e':
            return 'w'
        elif direction == 'w':
            return 'e'

    # this method creates an object with the cardinal points avaiable in the room as keys, and initialize their values
    def cardinal_directions_obj(current_room, my_rooms_graph):
        my_rooms_graph[current_room.id] = {}

        for exits in current_room.get_exits():
                my_rooms_graph[current_room.id][exits] = '?'
    
    my_rooms_graph = {}
    # as long as my rooms graph does not have 499 rooms visited...
    while(len(my_rooms_graph) < len(room_graph)):
        # we check if the current room's ID is not in our graph..
        if player.current_room.id not in my_rooms_graph:
            # if it is not, we create the cardinal directions object, initialized with '?' marks.
            cardinal_directions_obj(player.current_room, my_rooms_graph)

        unexplored_exits = [] # initially it will have ['n', 's', 'w', 'e'] since we start at room 0
        # we iterate over the exits available in the player's current room
        for next_exit in my_rooms_graph[player.current_room.id]:
            # and we check if it's value is a '?' mark, if it is...
            if my_rooms_graph[player.current_room.id][next_exit] == '?':
                # it means it's an unexplored room, so we add it to the unexplored exits array.
                unexplored_exits.append(next_exit)
        # we check if there is any unexplored exits, if there is...
        if len(unexplored_exits) != 0:
            # we randomly choose an unexplored exit
            new_exit = random.choice(unexplored_exits)
            # we append the random selection to the traversal path
            traversal_path.append(new_exit)
            # we use the 'get_room_in_direction' function to grab the room that point's to the chosen cardinal point
            next_room = player.current_room.get_room_in_direction(new_exit)
            # and we update our current location object's cardinal point to be equal to the next room's id 
            my_rooms_graph[player.current_room.id][new_exit] = next_room.id
            # we check if the next room's ID is not in our graph..
            if next_room.id not in my_rooms_graph:
                # if it is not, we make a new cardinal directions obj, initialized with '?' marks.
                cardinal_directions_obj(next_room, my_rooms_graph)
            # if it is in our graph, it means we have been there, so we update the next room's cardinal point to be the current room's ID.
            my_rooms_graph[next_room.id][opposite_direction(new_exit)] = player.current_room.id
            # then last but not least, we move to the unexplored exit
            player.travel(new_exit)
        else:
            # tis will run the BST in the current room, and determine a path to the next unexplored room.
            path = bread_first_traversal(my_rooms_graph)
            # we iterate over the ID's in our path
            for path_rooms_id in path:
                # we iterate over the exits in the player's current room
                for next_exit in my_rooms_graph[player.current_room.id]:
                    # we check if the next exit is in the graph
                    if next_exit in my_rooms_graph[player.current_room.id]:
                        # we check if the cardinal points values of our player's current location matches with any of the ID's in the path
                        if my_rooms_graph[player.current_room.id][next_exit] == path_rooms_id and player.current_room.id != path_rooms_id:
                            # if it does, we append the cardinal point where we are moving to the traversal path
                            traversal_path.append(next_exit)
                            # we grab the next room
                            next_room = player.current_room.get_room_in_direction(next_exit)
                            # we set the cardinal point's value where we are moving to be equal to the next room's ID
                            my_rooms_graph[player.current_room.id][next_exit] = next_room.id
                            # we check if the next room is in our graph, if it is...
                            if next_room.id not in my_rooms_graph:
                                # we create an object with cardinal points, initialized with '?' marks
                                cardinal_directions_obj(next_room, my_rooms_graph)
                            # if it is in our graph, it means we have been there, so we update the next room's cardinal point to be the current room's ID.
                            my_rooms_graph[next_room.id][opposite_direction(next_exit)] = player.current_room.id
                            # and we move to the next unexplored exit
                            player.travel(next_exit)
    
traverse_world()



# TRAVERSAL TEST
my_rooms_graph = set()
player.current_room = world.starting_room
my_rooms_graph.add(player.current_room)
# As we move, it adds the current room to the visited
for move in traversal_path:
    player.travel(move)
    my_rooms_graph.add(player.current_room)

if len(my_rooms_graph) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(my_rooms_graph)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(my_rooms_graph)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")