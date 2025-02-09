import heapq as min_heap_esque_queue
import copy
import time

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

puzzle_15 = [[ 1,  2,  3,  4 ],
            [ 5,  6,  7,  8 ],
            [ 9, 10, 11, 12 ],
            [13,  0, 14, 15 ]]

def find_blank_position(puzzle):
    size = len(puzzle)
    for row in range(size):          
        for col in range(size):      
            if puzzle[row][col] == 0:
                return (row, col)    

class Node:
    def __init__(self, board, depth=0, heuristic=0, parent=None):
        self.board = [row[:] for row in board]  
        self.depth = depth
        self.heuristic = heuristic
        self.parent = parent
        self.children = []
    
    def get_board(self):
        return [row[:] for row in self.board]
    
    def get_depth(self):
        return self.depth
    
    def __lt__(self, other):
        self_depth_heuristic = (self.depth or 0) + (self.heuristic or 0)
        other_depth_heuristic = (other.depth or 0) + (other.heuristic or 0)
        return self_depth_heuristic < other_depth_heuristic

    def set_heuristic(self, value):
        self.heuristic = value
        
    def get_heuristic(self):
        return self.heuristic
        
    def get_parent(self):
        return self.parent
    
    def move(self, queueing_function):
        children = []
        row, col = find_blank_position(self.board)
        size = len(self.board)
    
        if (row+1 < size):
            copy_puzzle1 = copy.deepcopy(self.board)
            copy_puzzle1[row][col] = copy_puzzle1[row+1][col]
            copy_puzzle1[row+1][col] = 0
            newNode = Node(copy_puzzle1,self.depth+1,queueing_function(copy_puzzle1),self)
            children.append(newNode)
                
        if (row-1 >= 0) :
            copy_puzzle2 = copy.deepcopy(self.board)
            copy_puzzle2[row][col] = copy_puzzle2[row-1][col]
            copy_puzzle2[row-1][col] = 0
            newNode = Node(copy_puzzle2,self.depth+1,queueing_function(copy_puzzle2),self)
            children.append(newNode)
                
        if (col+1 < size) :
            copy_puzzle3 = copy.deepcopy(self.board)
            copy_puzzle3[row][col] = copy_puzzle3[row][col+1]
            copy_puzzle3[row][col+1] = 0
            newNode = Node(copy_puzzle3,self.depth+1,queueing_function(copy_puzzle3),self)
            children.append(newNode)
                
        if (col-1 >= 0) :
            copy_puzzle4 = copy.deepcopy(self.board)
            copy_puzzle4[row][col] = copy_puzzle4[row][col-1]
            copy_puzzle4[row][col-1] = 0
            newNode = Node(copy_puzzle4,self.depth+1,queueing_function(copy_puzzle4),self)
            children.append(newNode)
            
        return children
        

def run_timer():
    start_time = time.perf_counter()  # Get the start time with higher precision
    print("Timer started...")
    
    # Simulating some task or delay
    time.sleep(2)  # Replace with the actual task you want to time
    
    end_time = time.perf_counter()  # Get the end time
    
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Task completed in {elapsed_time:.3f} milliseconds.")

def main():
    run_timer
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')

    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Please only enter valid 8-puzzles. Enter the puzzle delimiting " +
              "the numbers with a space. RETURN when finished" + '\n')
        
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
                                "difficulty on a scale from 0 to 5." + '\n')
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
    if selected_difficulty == "5":
        print("Difficulty of '15-puzzle' selected.")
        return puzzle_15

def print_puzzle(puzzle):
    for i in range(0,len(puzzle)):
        print(puzzle[i])
    

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, " + 
                      "(2) for the Misplaced Tile Heuristic, " +
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == '1':
        general_search(puzzle, uniform_cost_search)
        
    if algorithm == '2':
        general_search(puzzle, misplaced_tile)
    
    if algorithm == '3':
        general_search(puzzle, manhattan_distance)
        

def generate_solved_state(size):
    solved_state = [[(i * size + j + 1) % (size * size) for j in range(size)] for i in range(size)]
    return solved_state


def misplaced_tile(puzzle):
    size = len(puzzle)  
    every_solved = generate_solved_state(size)
    
    count = 0
    solved_flat = [num for row in every_solved for num in row]  
    puzzle_flat = [num for row in puzzle for num in row]
    
    for i in range(len(solved_flat)):
        if solved_flat[i] != puzzle_flat[i] and puzzle_flat[i] != 0:
            count += 1
    
    return count

def manhattan_distance(puzzle):
    dist = 0
    size = len(puzzle)
    
    for row in range(size):
        for col in range(size):
            num = puzzle[row][col]
            if num != 0:
                exp_col = (num-1)%size
                exp_row = (num-1)//size
                dist += (abs(exp_row-row) + abs(exp_col-col))
            
    return dist

def uniform_cost_search(puzzle):
    return 0


def general_search(puzzle, queueing_function):
    start_time = time.perf_counter()
    starting_node = Node(puzzle, depth=0, heuristic=queueing_function(puzzle))
    working_queue = []
    repeated_states = dict()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    size = len(puzzle)
    
    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        current_node = min_heap_esque_queue.heappop(working_queue)
        
        print(f"The best state to expand with a g(n) = {current_node.get_depth()} and h(n) = {current_node.get_heuristic()} is...")
        print_puzzle(current_node.get_board())
        
        if current_node.get_board() == generate_solved_state(size):
            print("\nSolution found! Printing solution path:")
            stack_to_print = [current_node]
            iter_node = copy.deepcopy(current_node)
            while iter_node.get_parent() is not None:
                stack_to_print.append(iter_node.get_parent())
                iter_node = iter_node.get_parent()
                
            for element in reversed(stack_to_print):
                print(f"The best state to expand with a g(n) = {element.get_depth()} and h(n) = {element.get_heuristic()} is...")
                print_puzzle(element.get_board())
                
            print(f"Solution depth was {current_node.get_depth()}")
            print(f"Number of nodes expanded: {num_nodes_expanded}")
            print(f"Max queue size: {max_queue_size}")
            
            end_time = time.perf_counter()  # Get the end time
            elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"Task completed in {elapsed_time:.3f} milliseconds.")
            
            return
        
        current_node_tuple = tuple(map(tuple, current_node.get_board()))
        repeated_states[current_node_tuple] = True
        children = current_node.move(queueing_function)
        
        for child in children:
            child_state = tuple(map(tuple, child.get_board()))
            if child_state not in repeated_states:
                min_heap_esque_queue.heappush(working_queue, child)
                repeated_states[child_state] = True
                
        num_nodes_expanded += 1
    
    end_time = time.perf_counter()  # Get the end time
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Failed task completed in {elapsed_time:.3f} milliseconds.")
        
    return "failure"        
        
if __name__ == "__main__":
    main()