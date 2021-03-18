#https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3


def solution1(inp):
    pp=[]
    for s in inp.split(' '):
        ss=[]
        for i in range(len(s)):
            if i%2==0:
                ss.append( s[i].upper())
            else:
                ss.append(s[i].lower())
        pp.append(('').join(ss))
    return (' ').join(pp)


def solution(inp):
    return (' ').join([''.join([s[i].upper() if i%2==0 else s[i].lower() for i in range(len(s))]) for s in inp.split(' ')])


if __name__ == "__main__":
    example = "try hello world"
    print(solution(example)) #'TrY HeLlO WoRlD'
    

