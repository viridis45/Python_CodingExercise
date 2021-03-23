# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3


def solution(lis : list) -> list:
    lis.remove(min(lis))
    return lis if len(lis)>0 else [-1]


if __name__ == "__main__":
    solution([4,3,2,1]) #[4,3,2]