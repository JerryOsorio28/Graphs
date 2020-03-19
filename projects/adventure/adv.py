from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
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
# traversal_path = ['n', 'n']
traversal_path = []

def traverse_world():
    graph = {}
    # Create an empty stack
    cardinal_directions = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    graph[player.current_room.id] = cardinal_directions.copy()
    

    s = Stack()
    # Push the starting vertex_id to the stack
    s.push(player.current_room.id)
    # Create an empty set to store visited nodes
    visited = set()
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        # Check if it's been visited
        # If it has not been visited...
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            print('visited', visited)
            # Then push all neighbors to the top of the stack
            for exits in player.current_room.get_exits():
                if graph[player.current_room.id][exits] == '?':
                    # we copy the ID of the current room before moving (object)
                    prev_room_id = player.current_room.id
                    # we move to the next room
                    player.travel(exits)
                    if player.current_room.id not in visited:
                        # we update the previous room direction to match the current room's ID
                        graph[prev_room_id][exits] = player.current_room.id
                        # we add the current room to the graph 
                        graph[player.current_room.id] = cardinal_directions.copy()
                        # we push the current position ID to the stack
                        s.push(player.current_room.id)
                        print('my graph', graph)
                    
                # print('exits in current room', exits)
                # print('current room ID', player.current_room.id)
                # print('previous room', prev_room_id)
                # print('current room exits', graph[player.current_room.id][exits])

    # print('world', room_graph)
    # print('player current room Exits', player.current_room.get_exits())

traverse_world()



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# As we move, it adds the current room to the visited
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