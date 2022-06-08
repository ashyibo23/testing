
'''
number of 1 and 0 in the matrix

'''

def solution(mat):
    if not mat:
        return 0

    visited = set()
    count = 0


    def dfs(r, c , visit):
        if r < 0 or (r, c) in visited or c < 0 or c >= len(mat[0]) or r >= len(mat):
            return 

        if mat[r][c] == 1:
            visited.add((r, c))

            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)

    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 1 and (row, col) not in visited:
                dfs(row, col, visited)
                count +=1
    return count 



matrix = [[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1 ]]

print(solution(matrix))

# time complexity is m * n size of matrix 






























