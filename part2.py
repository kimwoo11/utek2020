import argparse
from src.parse_input import parse_p2
from src.out_writer import OutputWriterP2

class PartTwo:
    def insert(self, idx, char):
        return "Insert {}, '{}'".format(idx, char)
    
    def delete(self, idx):
        return "Delete {}".format(idx)
    
    def replace(self, idx, char):
        return "Replace {}, '{}'".format(idx, char)

    def matrixCompute(self, word1, word2):
        """
        Inputs:
            (word1 <str>, word2 <str>)
        
        Outputs:
            (memo <N+1 by M+1 array>, zero_len <boolean>), where N=len(word1) & M=len(word2)
        
        matrixCompute() computes the memoized matrix that stores the optimal solution
        (minimal number of operations) in memo[N][M]
        """
        
        n = len(word1)
        m = len(word2)

        # Array to cache the convertion history (memoization)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for i in range(n + 1):
            memo[i][0] = i
        for j in range(m + 1):
            memo[0][j] = j
        
        # Check if one of the words contain no characters
        if n * m == 0:
            return memo, True

        # Memoize!
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = memo[i - 1][j] + 1
                down = memo[i][j - 1] + 1
                left_down = memo[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                memo[i][j] = min(left, down, left_down)

        return memo, False
    
    def partTwo(self, word1, word2):
        """
        `part2` takes in two strings (word1 and word2) and outputs the optimal series of commands
        to convert word1 into word2. The following is a list of possible output commands:
        
        1. Insert <index>, '<char>'
        - Inserts <char> at the given <index>. For eg. Insert 1, ‘c’ on “brain” gives “bcrain”

        2. Delete <index>
        - Deletes the character at the given <index>

        3. Replace <index>, '<new-char>'
        - Replaces character at <index> with <new-char>
        
        The solution is an adaptation of the Levenshtein distance algorithm (matrixCompute()).
        """
        writer = OutputWriterP2()

        path = []
        n, m = len(word1), len(word2)
        memo, zero_len = self.matrixCompute(word1, word2)
        
        i, j = n, m 
        
        if zero_len:
            if n == 0:
                for i in range(m):
                    writer.insert(word2[i], i)
            else:
                for i in range(n):
                    writer.delete(0)

        else:
            # Backtrack to find optimal path
            path.insert(0, (n, m))
            while i > 0 and j > 0:
                left = memo[i][j-1] if j-1 >= 0 else float('inf')
                down = memo[i-1][j] if i-1 >= 0 else float('inf')
                diag = memo[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else float('inf')
                
                opt = min(left, down, diag)
                
                if opt == diag:
                    path.insert(0, (i-1,j-1))
                    j -= 1
                    i -= 1
                elif opt == down:
                    path.insert(0, (i-1, j))
                    i -= 1
                else:
                    path.insert(0, (i,j-1))
                    j -= 1 
            
            # Compute comands
            for idx in range(len(path)-1):
                i, j = path[idx]
                curr_num_operations = memo[i][j]

                delete = (i+1, j)
                replace = (i+1, j+1)

                next_coord = path[idx+1]
                next_num_operations = memo[next_coord[0]][next_coord[1]]

                if next_coord == replace:
                    if curr_num_operations != next_num_operations:
                        writer.replace(word2[i], i)
                elif next_coord == delete:
                    if curr_num_operations != next_num_operations:
                        writer.delete(i)
                else:
                    if curr_num_operations != next_num_operations:
                        writer.insert(word2[i], i)
            
            print(path)
            for i in range(len(memo)):
                print(memo[i])

            for i in range(len(memo)):
                y, x = path[i]
                print(memo[y][x])
            
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Librarians Dilemma')
    parser.add_argument('--input_path', required=True, help='Pass input file path to --input_path')
    args = parser.parse_args()    

    # Compute moves for given strings
    original, desired = parse_p2(args)
    print('Original: {}'.format(original))
    print('Desired: {}'.format(desired))
    p2 = PartTwo()
    p2.partTwo(word1=original, word2=desired)
