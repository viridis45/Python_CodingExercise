# https://programmers.co.kr/learn/courses/30/lessons/12950


def solution(arr1, arr2):
    ans = []
    for c,d in zip(arr1,arr2):
        ans.append([e+f for e,f in zip(c,d)])
    return ans


if __name__ == '__main__':
    solution([1,2],[2,3]],[[3,4],[5,6]) #[[4,6],[7,9]]