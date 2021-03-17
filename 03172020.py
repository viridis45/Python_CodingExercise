#https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3


def solution(n):
    return sum(set( [a for a in range(1,n+1) if n%a==0]))
    #return num + sum( [a for a in range(1,(n/2)+1) if n%(a)==0])


if __name__ == "__main__":
    return solution(12) #28
