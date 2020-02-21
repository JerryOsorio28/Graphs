from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = []

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

def explore_lab(trv_path):

    visited = set()
    player_location_history = []
    
    counter = 0

    # Create an empty queue
    queue = Queue()
    # Add the initial vertex to the path
    player_location_history.append(player.current_room)
    # print('path', path)
    # Then add the path to the queue, should be initialized as a empty list
    queue.enqueue(player_location_history)
    # # While the queue is not empty...
    while queue.size() > 0:
        # Dequeue, the first PATH
        player_location_history = queue.dequeue() 
        # GRAB THE LAST VERTEX FROM THE PATH
        last_room = player_location_history[-1]
        # else check if it's been visited
        if last_room not in visited:
            # print('last_room', last_room)
        # If it has not been visited...
            # Added to the visited dic
            visited.add(last_room)
            # iterate over the last vertex's neighbors..
            if player.current_room.n_to is not None:
                if player.current_room.n_to not in visited:
                    player.current_room = player.current_room.n_to
                    trv_path.append('n')
                    counter += 1
            elif player.current_room.w_to is not None:
                if player.current_room.w_to not in visited:
                    player.current_room = player.current_room.w_to
                    trv_path.append('w')
                    counter += 1
            elif player.current_room.e_to is not None:
                if player.current_room.e_to not in visited:
                    player.current_room = player.current_room.e_to
                    trv_path.append('e')
                    counter += 1
            elif player.current_room.s_to is not None:
                if player.current_room.s_to not in visited:
                    player.current_room = player.current_room.s_to
                    trv_path.append('s')
                    counter += 1
            # visited = [0,1,2]
            if player.current_room not in visited:
                # if it is not, we make a copy of the path
                copy_location_history = player_location_history.copy()
                # we append the neighbor to the copy of the path
                copy_location_history.append(player.current_room)
                # then we add the copy of the path to the queue
                queue.enqueue(copy_location_history)
            else:
                for i in range(counter):
                    print('counter', counter)
                    player.current_room = player.current_room.s_to
                counter = 0
            print('visited', visited)
            print('trv path', trv_path)
            # queue.enqueue(player.current_room)

            # if player.current_room not in visited:
            #     copy_location_history = player_location_history.copy()
            #     copy_location_history.append(player.current_room)
            #     queue.enqueue(copy_location_history)


    # print('current room', player.current_room)
            
explore_lab(traversal_path)

# print('traversal_path',traversal_path)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
