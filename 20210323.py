# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3
# filtering out minimium number

def solution(lis):
    lis2 = [a for a in lis if a!= min(lis)]
    return lis2 if len(lis2)>0 else [-1]


def solution2(lis:list)->list:
    minnum = min(lis)
    return [-1] if {minnum} == set(lis) else list(filter(lambda x: x!=minnum, lis))


if __name__ == "__main__":
    solution2([4,3,2,1]) #[4,3,2]