# Time Complexity : O(m * n), m is no of rows and n is no of columns
# Space Complexity : O(m * n), because the queue can store all leaf nodes at worst
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:


from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        if mat is None:
            return mat
        
        m = len(mat)
        n = len(mat[0])
        q = deque()
        lvl = 0

        # directions to check for the adjacent neighbours
        dirs = [[-1, 0], [1, 0], [0,-1], [0, 1]]

        # traversing the matrix
        for i in range(m):
            for j in range(n):
                # looking for all 0's to put in queue at lvl = 0, because 0's are independent 
                if mat[i][j] == 0:
                    q.append([i, j])
                # looking for all 1's to make them -1
                if mat[i][j] == 1:
                    mat[i][j] = -1
        # bfs
        while q:
            # need size variable to keep track of distance of 1's from 0's
            # distinction between lvls
            size = len(q)
            for i in range(size):
                curr = q.popleft() # list of coordinates
                # looking for adjacent neighbours
                for dir in dirs:
                    # nr and nc are coordinates of a neighbour
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1:
                        # add to queue, the coordinates of 1 neighbour
                        q.append([nr, nc])
                        # update the contents of this cell by the distance of nearest 0
                        mat[nr][nc] = lvl + 1
            
            # after completing every level
            lvl += 1
        
        return mat


        

        