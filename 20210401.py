# https://programmers.co.kr/learn/courses/30/lessons/12954


def solution(a, b):
    answer = [a+(a*i) for i in range(b) ]
    return answer


if __name__ == '__main__':
    solution(2,5) # [2,4,6,8,10]



# https://leetcode.com/problems/find-center-of-star-graph/submissions/
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return list(set(edges[0]).intersection(edges[1]))[0]

# li = [[1,2],[5,1],[1,3],[1,4]]
# a = Solution()
# a.findCenter(li)
