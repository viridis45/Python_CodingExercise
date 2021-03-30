# https://programmers.co.kr/learn/courses/30/lessons/12948


def solution(a):
    return '*'*(len(a)-4)+a[-4:]


if __name__ == '__main__':
    solution('027778888') #'******8888'