def solution(n,words):
    used=[words[0]]
    for i,w in enumerate(words[1:]):
        now_turn = ((i+1)//n)+1
        now_p = (i+2)%n
        if now_p == 0:
            now_p = n
        if used[-1][-1]!=w[0] or w in used:
            return [now_p,now_turn]
        used.append(w)
    return [0,0]