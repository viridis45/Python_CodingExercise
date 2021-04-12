# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    br, ca, wg = bridge_length, weight, truck_weights
    totwgt, lastcarnum,carnumOnBg, crs,ct = 0,0,0,[],0
    totlen = len(wg)
    while lastcarnum<totlen: # counting till the last car enters the bridge
        if carnumOnBg==br: # when the bridge is full
            totwgt-=crs.pop(0) # first car exits
            carnumOnBg-=1
        if totwgt+wg[lastcarnum] <= ca: #if bridge can hold the next car weight
            totwgt+=wg[lastcarnum]
            crs.append(wg[lastcarnum])
            lastcarnum+=1
            carnumOnBg+=1
        else: # filling up the bridge
            carnumOnBg+=1
            crs.append(0) # 0 is count as a 'car', but as a placeholder.
        ct+=1
    return ct+br # counting till the last car exits the bridge


if __name__ == '__main__':
    solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) #110
    #  2,10,[7,4,5,6], 8