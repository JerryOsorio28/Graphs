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

def explore_lab(visited=None, path=None, trv_path=None, all_rooms=None, prev_room=None):

    graph = {}

    room_exits = {}

    if all_rooms is None:
        all_rooms = []

    if trv_path is None:
        trv_path = []
    
    if visited is None:
        visited = []

    if path is None:
        path = []
    
    if prev_room is None:
        prev_room = []

    if player.current_room not in all_rooms:
        # we append our starting vertex to the path
        all_rooms.append(player.current_room)
        path.append(player.current_room)
        print('first path', path)
        # print('HWHATS player.current_room', player.current_room.id)
    # we grab the last value in our path
    if len(all_rooms) == 9:
        print('trv_path', trv_path)
        return trv_path

    for exits in player.current_room.get_exits():
        # print('exits', exits)
        if exits == 'n':
            if player.current_room.n_to is not None and player.current_room.n_to not in all_rooms:
                if player.current_room not in visited:
                    visited.append(player.current_room)
                    prev_room.append(player.current_room)
                player.current_room = player.current_room.n_to
                trv_path.append('n')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
        elif exits == 's':
            if player.current_room.s_to is not None and player.current_room.s_to not in all_rooms:
                if player.current_room not in visited:
                    visited.append(player.current_room)
                    prev_room.append(player.current_room) 
                player.current_room = player.current_room.s_to
                trv_path.append('s')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
        elif exits == 'w':
            if player.current_room.w_to is not None and player.current_room.w_to not in all_rooms:
                if player.current_room not in visited:
                    visited.append(player.current_room)
                    prev_room.append(player.current_room) 
                player.current_room = player.current_room.w_to
                trv_path.append('w')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
        elif exits == 'e':
            if player.current_room.e_to is not None and player.current_room.e_to not in all_rooms:
                if player.current_room not in visited:
                    visited.append(player.current_room)
                    prev_room.append(player.current_room) 
                player.current_room = player.current_room.e_to
                trv_path.append('e')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
        # print('What is north???', player.current_room.n_to)
        if player.current_room not in visited:
            visited.append(player.current_room)
            prev_room.append(player.current_room)
            # print('visited', visited)
        while player.current_room in visited:
            if player.current_room != 'Room 0':
                # path.pop()
                visited.pop()
                prev_room.pop()
                print('What is path here???', path)
                print('visited', visited)
                print('trv path', trv_path)
                print("all_rooms", all_rooms)
                print("Players current location", player.current_room)
                if trv_path[-1] == 'n':
                    if len(visited) > 0:
                        if player.current_room.s_to == visited[-1]:
                            trv_path.append('s')
                            player.current_room = visited[-1]
                            # if player.current_room not in visited:
                            #     visited.append(player.current_room)
                            #     prev_room.append(player.current_room)
                            explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                        else:
                            trv_path.append('n')
                            player.current_room = path[-1]
                            explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                      
                elif trv_path[-1] == 's':
                    if len(visited) > 0:
                        print('Passed?', True)
                        if player.current_room.n_to == visited[-1]:
                            trv_path.append('n')
                            player.current_room = visited[-1]
                            # if player.current_room not in visited:
                            #     visited.append(player.current_room)
                            #     prev_room.append(player.current_room)
                            explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                        else:
                            trv_path.append('s')
                            player.current_room = visited[-1]
                            explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                # elif trv_path[-1] == 'w':
                #     if player.current_room.e_to == path[-1]:
                #         trv_path.append('e')
                #         player.current_room = path[-1]
                #         explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                #     else:
                #         trv_path.append('w')
                #         player.current_room = path[-1]
                #         explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)

                # elif trv_path[-1] == 'e':
                #     if player.current_room.w_to == path[-1]:
                #         trv_path.append('w')
                #         player.current_room = path[-1]
                #         explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)
                #     else:
                #         trv_path.append('e')
                #         player.current_room = path[-1]
                #         explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms, prev_room=prev_room)


    # print('prev_room', prev_room)
    # print('visited', visited)
    # print('trv path', trv_path)
    # print('players current room ID', player.current_room.id)
    # # print('Exits for current rooms', player.current_room.get_exits())
    # # print('Players direction', player.travel(direction))
    # print("Players current location", player.current_room)
    # print('graph', graph)
explore_lab()

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
