import heapq as min_heap_esque_queue

sovled = [[1, 2, 3],
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
            
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
    
    return

def init_default_puzzle_mode():
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired " +
                                "difficulty on a scale from 0 to 5." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Solved' selected.")
        return sovled
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
    
    
if __name__ == "__main__":
    main()