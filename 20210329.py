# https://programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    a, b = x, 0
    while a>0:
        b+=a%10
        a//=10
    return x % b ==0


if __name__ == '__main__':
    solution(12) #true