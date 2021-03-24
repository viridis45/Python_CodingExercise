# https://programmers.co.kr/learn/courses/30/lessons/12937


def solution(num):
    return 'Odd' if num%2==1 else 'Even'


# 스쳐지나가셨으므로
#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
class Solution:
    def minOperations(self, b: str) -> List[int]:
        one_loc = [i for i,j in enumerate(b) if j=='1']
        return [int(sum([ abs(i-j) for j in one_loc])) for i in range(len(b))]
