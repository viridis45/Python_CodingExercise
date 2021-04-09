# https://programmers.co.kr/learn/courses/30/lessons/17682


def solution(dartResult):
    mods1={'S':1, 'D':2, 'T':3}
    mods2={'*':2,'#':-1}
    inp, sc, tot  = dartResult,'0',[]
    for i in inp:
        if (i).isdigit():
            sc+=i
            continue
        if i in ['S', 'D', 'T']:
            tot.append(int(sc)**mods1[i])
            sc='0'
        if i in ['*','#']:
            tot[-1]=tot[-1]*mods2[i]
            if i=='*' and len(tot)>1:
                tot[-2]=tot[-2]*mods2[i]
    return sum(tot)


if __name__ == '__main__':
    solution("1T2D3D#") #-4



# 다른사람 풀이. regex를 통해 규칙이 있도록 바꾸어 한번에 연산.
import re
def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
