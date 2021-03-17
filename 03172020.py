https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3


def solution(n):
    answer = sum(set( [a for a in range(1,n+1) if n%(a)==0]))
    return answer



if __name__ == "__main__":
    return solution(12) #28
