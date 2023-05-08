def solution(n,words):
    said=[] 
    for i,w in enumerate(words):
        if not said:
            said.append(w)
        else:
            if w in said or len(w)==1 or w[0]!=said[-1][-1]:
                return [i%n+1,i//n+1]
        said.append(w)
    return [0,0]
      
