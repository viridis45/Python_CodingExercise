# https://leetcode.com/problems/max-increase-to-keep-city-skyline


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:        
        leng = len(grid)
        horiz = [max(i) for i in grid]
        vert = [max([i[j] for i in grid]) for j in range(leng)]
        indiv = [[min(horiz[i],vert[j]) for i in range(leng)] for j in range(leng)]
        exp = sum([min(horiz[i],vert[j]) for i in range(leng) for j in range(leng)])
        orig = sum([sum(i) for i in grid])
        return exp-orig