import argparse
import copy
from src.parse_input import *

def main(arguments):
    pass


def count_swiches(ops):

    # This function takes in a list of operations, and returns the number of operation switches and deletions

    curr = ops[0]
    count = 0
    del_count = 0

    for idx in range(len(ops)):
        # Iterate through every operation in the list

        nxt = curr[idx]
        # Get the next operation

        if nxt == 'D':
            del_count += 1

        if nxt == curr:
            # If the next operation is the same as the current one, no switches
            # Therefore don't do anything
            pass

        else:
            # Otherwise, there was a switch, which must be taken into account
            # NOTE: 'IIINDDDD' is one switch (from inserts to deletes) and not
            # two switches (from inserts to nothing to deletes)
            curr = nxt

            if nxt != 'N':
                # If not 'N', we need to take this into account
                count += 1

    return count, del_count

def get_solutions(m, solutions, row, col, current_solution_index):
    print("My position: " + str(row) + ", " + str(col))
    if row == len(m)-1 and col == 0:
        return

    curr_val = m[row][col][0]
    curr_solution = copy.deepcopy(solutions[current_solution_index])
    optimal_val = float('inf')
    
    left_val = float('inf')
    down_val = float('inf')
    diag_val = float('inf')

    if col > 0 and m[row][col-1][1][1]:
        left_val = m[row][col-1][0]
    if row < len(m) - 1 and m[row+1][col][1][0]:
        down_val = m[row+1][col][0]
    if col > 0 and row < len(m) - 1 and m[row+1][col-1][1][2]:
        diag_val = m[row+1][col-1][0]

    optimal_val = min(left_val, down_val, diag_val)
    num_optimal_solutions = 0

    if left_val == optimal_val:
        solutions[current_solution_index].insert(0, 'I') if left_val != curr_val else new_sol.insert(0, 'NI')
        num_optimal_solutions += 1
        get_solutions(m, solutions, row, col-1, current_solution_index)
    if down_val == optimal_val:
        new_sol = []
        if num_optimal_solutions > 0:
            new_sol = copy.deepcopy(curr_solution)
            new_sol.insert(0, 'D') if down_val != curr_val else new_sol.insert(0, 'ND')
            solutions.append(new_sol)
            get_solutions(m, solutions, row+1, col, len(solutions)-1)
        else:
            solutions[current_solution_index].insert(0, 'D') if down_val != curr_val else solutions[current_solution_index].insert(0, 'ND')
            get_solutions(m, solutions, row+1, col, current_solution_index)
        num_optimal_solutions += 1
    if diag_val == optimal_val:
        new_sol = []
        if num_optimal_solutions > 0:
            new_sol = copy.deepcopy(curr_solution)
            new_sol.insert(0, 'R') if diag_val != curr_val else new_sol.insert(0, 'NR')
            solutions.append(new_sol)
            get_solutions(m, solutions, row+1, col-1, len(solutions)-1)
        else:
            solutions[current_solution_index].insert(0, 'R') if diag_val != curr_val else solutions[current_solution_index].insert(0, 'NR')
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
