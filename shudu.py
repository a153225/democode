
def findShudu(initv):
    m=[[{1,2,3,4,5,6,7,8,9} for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if initv[i][j]>0:
                m[i][j]={initv[i][j]}
                for x in range(9):
                    if x!=j and initv[i][x] == initv[i][j]:return None
                    if x!=i and initv[x][j] == initv[i][j]:return None
                    if int(i/3)*3+int(x/3)!=i or int(j/3)*3+x%3 != j:
                        if initv[int(i/3)*3+int(x/3)][int(j/3)*3+x%3] == initv[i][j]:return None
            else:
                for x in range(9):
                    if initv[i][x] in m[i][j]:m[i][j].remove(initv[i][x])
                    if initv[x][j] in m[i][j]:m[i][j].remove(initv[x][j])
                    if initv[int(i/3)*3+int(x/3)][int(j/3)*3+x%3] in m[i][j]:m[i][j].remove(initv[int(i/3)*3+int(x/3)][int(j/3)*3+x%3])
                if len(m[i][j])==1:
                    T=m[i][j].pop()
                    initv[i][j]=T
                    m[i][j].add(T)
                elif len(m[i][j])==0:
                    return None
    isOk=True
    for i in range(9):
        for j in range(9):
            if len(m[i][j])!=1:
                isOk=False
                break
        if not isOk:
            break
    if isOk:
        return m

    for i in range(9):
        for j in range(9):
            if len(m[i][j])>1:
                for T in m[i][j]:
                    initv[i][j]=T
                    ret=findShudu([[v for v in row] for row in initv])
                    if ret:
                        return ret
                return None

if __name__=="__main__":
    v=[[0,0,6,7,0,0,0,0,2],
       [0,2,0,0,0,0,9,0,0],
       [4,0,0,3,0,0,0,1,0],
       [0,0,8,0,0,2,0,0,0],
       [6,3,0,0,5,0,0,0,0],
       [0,1,0,0,0,0,4,0,6],
       [0,0,4,0,0,9,0,0,8],
       [0,6,0,1,4,0,0,7,0],
       [0,0,0,0,8,0,1,0,0]]
    for row in findShudu(v):
        print(row)
