# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    score, res=[],stages
    players = len(stages)
    for i in range(1,N+1):
        a = res.count(i)
        score.append(a/players)
        players -= a
    
    scored = {a+1:b for a,b in enumerate(score)}
    ans = sorted(scored, key=lambda x : scored[x], reverse=True)
    return ans


if __name__ == '__main__':
    solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) #[3,4,2,1,5]
