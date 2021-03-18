#https://programmers.co.kr/learn/courses/30/lessons/42748

# 첫 번째 시도
def solution(array, commands):
    a = []
    for i in commands:
        arr = array[ i[0]-1:i[1] ]
        arr.sort()
        if (i[2]-1) > len(arr):
            a.append(arr[-1])
        else:
            a.append(arr[i[2]-1])
    return a

# 통과 후 두 번째 시도
def solution2(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]


# 첫 번째 코드가 더 빨리 돌았다고 합니다.
if __name__ == "__main__":
    ar = 	[1, 5, 2, 6, 3, 7, 4]
    com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(ar, com) #solution2(ar, com)
