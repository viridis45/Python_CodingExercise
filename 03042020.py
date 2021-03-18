#https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3


def solution(inp):
    threes = []
    while inp>0:
        threes.append(inp%3)
        inp=int(inp/3)
    while threes[0] == 0:   
        threes = threes[1:]
    answer = sum([3**a * threes[-(a+1)] for a in range(len(threes))])

    return answer


if __name__ == "__main__":
    solution(45) #7
