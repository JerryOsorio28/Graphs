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

def explore_lab(visited=None, path=None, trv_path=None, all_rooms=None):

    graph = {}

    room_exits = {}

    if all_rooms is None:
        all_rooms = []

    if trv_path is None:
        trv_path = []
    
    if visited is None:
        visited = set()

    if path is None:
        path = []

    # if player.current_room.n_to is not None:
    #     player.current_room = player.current_room.n_to
    #     traversal_path.append('n')
        # print(player.current_room)

    if player.current_room not in all_rooms:
        # we append our starting vertex to the path
        all_rooms.append(player.current_room)
        path.append(player.current_room)
    # we grab the last value in our path
    if len(all_rooms) == 9:
        print('path', path)
        return path

    last_room = path[-1]
    # # we check if the vertex (node) is in visited
    # if last_room not in visited:    
    #     # if it is not,3 we added to the set
    #     visited.add(last_room)

    for exits in player.current_room.get_exits():
        print('exits', exits)
        if exits == 'n':
            if player.current_room.n_to is not None and player.current_room.n_to not in all_rooms:
                if player.current_room not in visited:
                    visited.add(last_room)
                player.current_room = player.current_room.n_to
                trv_path.append('n')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms)
        elif exits == 's':
            if player.current_room.s_to is not None and player.current_room.s_to not in all_rooms:
                if player.current_room not in visited:
                    visited.add(last_room)
                player.current_room = player.current_room.s_to
                trv_path.append('s')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms)
            else:
                visited.add(last_room)
                prev_room = player.current_room
                while prev_room in visited:
                    if prev_room != 'Room 0':
                        player.current_room = player.current_room.s_to
                        visited.pop()
                        path.pop()
                        trv_path.append('s')
                    else:
                        explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms)

        elif exits == 'w':
            if player.current_room.w_to is not None and player.current_room.w_to not in all_rooms:
                player.current_room = player.current_room.w_to
                trv_path.append('w')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms)
        elif exits == 'e':
            if player.current_room.e_to is not None and player.current_room.e_to not in all_rooms:
                player.current_room = player.current_room.e_to
                trv_path.append('e')
                explore_lab(visited=visited, path=path, trv_path=trv_path, all_rooms=all_rooms)

        print('visited', visited)
        print('trv path', trv_path)
                
            # if exits == 'e':
            #     player.current_room = player.current_room.e_to
            # if exits == 'w':
            #     player.current_room = player.current_room.w_to
            # if exits == 's':
            #     player.current_room = player.current_room.s_to
        # return graph

        # we check if the neighbors are in the visited set...
        # if neighbor not in visited:
        #     # if they are NOT, we call the function recursively on it.
        #     self.dfs_recursive(neighbor, destination_vertex, path=path, visited=visited)
        # if neighbor in path:
        #     path.pop()

    print('players current room ID', player.current_room.id)
    # print('Exits for current rooms', player.current_room.get_exits())
    # print('Players direction', player.travel(direction))
    print("Players current location", player.current_room)
    print('graph', graph)
explore_lab()

print('traversal_path',traversal_path)


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
