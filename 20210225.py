# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()    
    for a,b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1]


if __name__ == "__main__":
    p = ["mislav", "stanko", "mislav", "ana"]
    c = ["stanko", "ana", "mislav"]
    solution(p,c)