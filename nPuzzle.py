import heapq as min_heap_esque_queue
import copy
# import networkx as nx
# import matplotlib.pyplot as plt

solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

light = [[1, 2, 3],
         [4, 5, 6],
         [7, 0, 8]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

medium = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

hard =  [[8, 7, 1],
         [6, 0, 2],
         [5, 4, 3]]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')

    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Please only enter valid 8-puzzles. Enter the puzzle delimiting " +
              "the numbers with a space. RET when finished" + '\n')
        
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")
        
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()
        
        for i in range(0,3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])
            
        user_puzzle = [ puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
    
    return

def init_default_puzzle_mode():
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired " +
                                "difficulty on a scale from 0 to 4." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Solved' selected.")
        return solved
    if selected_difficulty == "1":
        print("Difficulty of 'Light' selected.")
        return light
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Medium' selected.")
        return medium
    if selected_difficulty == "4":
        print("Difficulty of 'Hard' selected.")
        return hard

def print_puzzle(puzzle):
    for i in range(0,3):
        print(puzzle[i])
    print("\n")
    

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, " + 
                      "(2) for the Misplaced Tile Heuristic," +
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == '1':
        print(manhattan_distance(puzzle))
        # uniform_cost_search(puzzle, 0)
        
        
def find_blank_position(puzzle):
    for i in range(3):          
        for j in range(3):      
            if puzzle[i][j] == 0:
                return (i, j)    

def move_puzzle(puzzle, direction):
    copy_puzzle = copy.deepcopy(puzzle)
    row, col = find_blank_position(puzzle)
    
    if direction == "up":
        if (row+1 < 3):
            copy_puzzle[row][col] = copy_puzzle[row+1][col]
            copy_puzzle[row+1][col] = 0
            
    if direction == "down":
        if (row-1 >= 0) :
            copy_puzzle[row][col] = copy_puzzle[row-1][col]
            copy_puzzle[row-1][col] = 0
            
    if direction == "left":
        if (col+1 < 3) :
            copy_puzzle[row][col] = copy_puzzle[row][col+1]
            copy_puzzle[row][col+1] = 0
            
    if direction == "right":
        if (col-1 >= 0) :
            copy_puzzle[row][col] = copy_puzzle[row][col-1]
            copy_puzzle[row][col-1] = 0
            
    return copy_puzzle

def misplaced_tile(puzzle):
    count = 0
    solved_flat = [num for row in solved for num in row]  
    puzzle_flat = [num for row in puzzle for num in row]
    
    for i in range(len(solved_flat)):
        if solved_flat[i] != puzzle_flat[i]:
            count += 1
    
    return count

def manhattan_distance(puzzle):
    dist = 0
    
    for row in range(3):
        for col in range(3):
            num = puzzle[row][col]
            if num > 0:
                print(f"Num: {num}")
                exp_y = (num-1)%3
                print(f"exp_y: {exp_y}")
                exp_x = (num-1)//3
                print(f"exp_x: {exp_x}")
                print(abs(exp_x-row) + abs(exp_y-col))
                dist += (abs(exp_x-row) + abs(exp_y-col))
            
    return dist

# def queueing_function(nodes, new_nodes, heuristic):
#     for new_state, g_cost in new_nodes:
#         h_

def general_search(puzzle, queueing_function):
    starting_node = tuple(map(tuple, puzzle))
    working_queue = []
    min_heap_esque_queue.heappush(working_queue, (0, starting_node))

                
def uniform_cost_search(puzzle, heuristic):
    starting_node = tuple(map(tuple, puzzle))  
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, (0, starting_node))
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node] = True
    solved_puzzle = puzzle

    stack_to_print = []

    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        cost, node_from_queue = min_heap_esque_queue.heappop(working_queue)
        solved_tuple = tuple(map(tuple, solved))
        if node_from_queue == solved_tuple:
            solved_puzzle = node_from_queue
            print(f"Cost: {cost}")
            break

        node_as_list = [list(row) for row in node_from_queue]  

        for direction in ["up", "down", "left", "right"]:
            new_puzzle = move_puzzle(node_as_list, direction)  
            new_state = tuple(map(tuple, new_puzzle))  

            if new_state not in repeated_states:
                min_heap_esque_queue.heappush(working_queue, (cost + 1, new_state))
                repeated_states[new_state] = True
                print_puzzle(new_puzzle)

        num_nodes_expanded += 1

    print_puzzle(solved_puzzle)
    print(f"Total nodes expanded: {num_nodes_expanded}")

if __name__ == "__main__":
    main()