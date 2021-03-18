#https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3


def solution(a):
    lena = len(a)//2
    return a[lena-1: lena+lena%2+1]


if __name__ == "__main__":
    solution('qwer') #'we'
