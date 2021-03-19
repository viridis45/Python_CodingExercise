#https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3


def solution(n):
    return sum([int(i) for i in str(n)])


if __name__ == "__main__":
    example = "987"
    print(solution(example)) #24
    
