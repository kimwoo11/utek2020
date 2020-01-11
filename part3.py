import argparse
import copy
from src.parse_input import *

def main(arguments):
    pass


def get_solutions(m, solutions, row, col, current_solution_index):
    if row == len(m)-1 and col == 0:
        return

    curr_val = m[row][col]
    curr_solution = copy.deepcopy(solutions[current_solution_index])
    optimal_val = float('inf')
    
    left_val = float('inf')
    down_val = float('inf')
    diag_val = float('inf')

    if col > 0:
        left_val = m[row][col-1]
    if row < len(m) - 1:
        down_val = m[row+1][col]
    if col > 0 and row < len(m) - 1:
        diag_val = m[row+1][col-1]

    optimal_val = min(left_val, down_val, diag_val)
    num_optimal_solutions = 0

    if left_val == optimal_val:
        solutions[current_solution_index].append('I') if left_val != curr_val else new_sol.append('N')
        num_optimal_solutions += 1
        get_solutions(m, solutions, row, col-1, current_solution_index)
    if down_val == optimal_val:
        new_sol = []
        if num_optimal_solutions > 0:
            new_sol = copy.deepcopy(curr_solution)
            new_sol.append('D') if down_val != curr_val else new_sol.append('N')
            solutions.append(new_sol)
            get_solutions(m, solutions, row+1, col, len(solutions)-1)
        else:
            solutions[current_solution_index].append('I') if down_val != curr_val else new_sol.append('N')
            get_solutions(m, solutions, row+1, col, current_solution_index)
        num_optimal_solutions += 1
    if diag_val == optimal_val:
        new_sol = []
        if num_optimal_solutions > 0:
            new_sol = copy.deepcopy(curr_solution)
            new_sol.append('R') if diag_val != curr_val else new_sol.append('N')
            solutions.append(new_sol)
            get_solutions(m, solutions, row+1, col-1, len(solutions)-1)
        else:
            solutions[current_solution_index].append('R') if diag_val != curr_val else new_sol.append('N')
            get_solutions(m, solutions, row+1, col-1, current_solution_index)
        num_optimal_solutions += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Librarians Dilemma')
    parser.add_argument('--input_path', required=True, help='Pass input file path to --input_path')
    args = parser.parse_args()
    #original, desired = parse(args)

    #m = get_matrix(original, desired)
    m = [[5,4,4,3],[4,3,3,2],[3,2,2,2],[2,2,1,2],[1,1,2,3],[0,1,2,3]]
    solutions = [[]]
    get_solutions(m, solutions, 0, len(m[0])-1, 0)
    print(solutions)
