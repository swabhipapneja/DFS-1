# Time Complexity : O(m * n), m is no of rows and n is no of columns
# Space Complexity : O(m * n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:


from collections import deque

class Solution(object):
    def __init__(self):
        self.m = 0
        self.n = 0
        self.dirs = [[-1,0], [1, 0], [0, -1], [0, 1]]

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

        self.m = len(image)
        self.n = len(image[0])
        
        # recursive solution
        self.dfs(image, sr, sc, color, image[sr][sc])        
        return image
    
    def dfs(self, image, sr, sc, color, oldcolor):
        # base case, if the new row/column becomes invalid
        # or if the value is not same as old color => we return
        if sr < 0 or sr == self.m or sc < 0 or sc == self.n or image[sr][sc] != oldcolor:
            return

        # now it means the current element has value of old color
        # so we change it's value to to color
        image[sr][sc] = color
        # checking for all neighbours
        for dir in self.dirs:
            nr = sr + dir[0]
            nc = sc + dir[1]
            # checking recursively for all neighbours
            self.dfs(image, nr, nc, color, oldcolor)
        

