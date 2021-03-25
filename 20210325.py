# https://programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    def getdist(a, b):
        x1, x2 = ((a+2)%3)+1, ((b+2)%3)+1
        y1, y2 = (a-1)//3+1, (b-1)//3+1
        return (((x1 - x2)**2)**(1/2))+(((y1 - y2)**2)**(1/2)) #절대값

    def main(numbers:list, hand:str)->list:
        L, R, trace = 11, 12, []
        for i in numbers:
            if i == 0 :
                i = 11
            if i in [1,4,7,10]:
                L = i
                trace.append('L')
            elif i in [2,5,8,11]:
                Ld, Rd = getdist(L, i), getdist(R,i)
                if Ld<Rd or (Ld==Rd and hand=='left'):
                    L = i
                    trace.append('L')
                else:
                    R = i
                    trace.append('R')
            else:
                R = i
                trace.append('R')
        return ''.join(trace)
    ans = main(numbers, hand)
    return ans