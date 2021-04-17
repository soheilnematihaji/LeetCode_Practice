def edit_distance(s1,s2):
    n=len(s1)
    m=len(s2)
    d=[[0 for i in range(m+2) ] for j in range(n+2)]
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            if i==n:
                d[i][j]=m-j
            elif j==m:
                d[i][j]=n-i
            elif s1[i]==s2[j]:
                d[i][j]=d[i+1][j+1]
            else:
                l1=1+d[i+1][j+1]
                l2=1+d[i][j+1]
                l3=1+d[i+1][j]
                d[i][j]=min(l1,l2,l3)
    return d[0][0]
