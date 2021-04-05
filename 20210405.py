# https://www.acmicpc.net/problem/9466

import sys
#sys.setrecursionlimit(10000)


# 사람1부터 선택한 번호를 보고 그 번호부터 꼬리물기를 생성. 
# 꼬리물기가 우로보로스가 되지 않는 경우 다음 번호으로 넘어감. 
# 우로보로스가 생성되는경우 그룹화된 사람 리스트에 추가
# 그룹화되지 않은 사람들을 프린트


def cycle(pNum, checked):
    if checked[pNum] == True:    # 무는 꼬리가 이미 본 적 있는 꼬리일 경우 그만둔다
        if pNum in checkedList:
            groupedppl.extend(checkedList[checkedList.index(pNum):])
        return
    checked[pNum] = True
    nextNum = prefN[pNum]
    checkedList.append(pNum)
    cycle(nextNum, checked)


if __name__ == '__main__':
    trials = int(input('테스트 케이스의 개수 T :')) # 1
    for _ in range(trials):
        totN = int(input(' 순열의 크기 N : ')) # totN = 7
        inp = input('순열의 개수 : ') #inp = '3 1 3 7 3 4 6'
        checked = [0]*(totN+1)
        prefN = [0] + list(map(int, inp.split(' ')))
        groupedppl=[]

        for i in range(1,totN+1):
            if checked[i]==False:
                checkedList = []
                cycle(i, checked)
        print(totN - len(groupedppl))# 3
