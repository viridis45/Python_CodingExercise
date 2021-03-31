# https://programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    minnum, maxnum= min(a,b), max(a,b)
    return sum(range(minnum, maxnum+1))


if __name__ == '__main__':
    solution(5,3) #12