class PartTwo:
    def __init__(self):
        self.res = []

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
            (d <N by M array>, zero_len <boolean>)
        """
        
        n = len(word1)
        m = len(word2)
        
        # Array to cache the convertion history (memoization)
        d = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        
        # Check if one of the words contain no characters
        if n * m == 0:
            return d, True

        # Memoize!
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        
        return d, False
    
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
        
        The solution is an adaptation of the Levenshtein distance algorithm.
        """
        
        