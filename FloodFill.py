# Time Complexity : O(m * n), m is no of rows and n is no of columns
# Space Complexity : O(m * n), because the queue can store all leaf nodes at worst
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:


from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image is None or image[sr][sc] == color:
            return image
        
        m = len(image)
        n = len(image[0])

        # queues to store the row and col indices
        row = deque([sr])
        col = deque([sc])

        # save the old color before changing
        oldcolor = image[sr][sc]

        # change the starting element's color from oldcolor to color 
        image[sr][sc] = color

        # dirs array to look at adjacent neighbors
        dirs = [[-1,0], [1,0], [0, -1], [0, 1]]

        while row:
            # getting the indices of the starting element
            currRow = row.popleft()
            currCol = col.popleft()

            # now look at all neighbours
            for dir in dirs:
                nr = currRow + dir[0]
                nc = currCol + dir[1]
                # if the neighbour indices are valid, and they have the old colour value
                if nr >= 0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == oldcolor:
                    # then update to new colour
                    image[nr][nc] = color
                    row.append(nr)
                    col.append(nc)
        
        return image