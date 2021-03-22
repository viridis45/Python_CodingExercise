# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3


def solution(n : int) -> int:
    inp2 = n**(1/2)
    return int((inp2+1)**2) if inp2 == int(inp2) else -1


if __name__ == "__main__":
    solution(121) #144