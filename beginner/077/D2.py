K =int(input())
A = [1]
B = [[x,0] for x in range(K)]
C = [1]
if K == 1:
    print(1)
else:
    B[1][1] = 1
    while B[0][1] == 0:
        for x in C:
            b = (10*x)%K
            c = (x+1)%K
            if b == 0:
                B[0][1] = B[x][1]
                print("A")
                break
            elif c == 0:
                B[0][1] = B[x][1] + 1
                print("B")
                break
            else:
                print(b)
                print(c)
                if b in C:
                    pass
                else:
                    C += [b]
                    B[b][1] = B[x][1]
                if c in C:
                    pass
                else:
                    C += [c]
                    B[c][1] = B[x][1] + 1
    print(B[0][1])                
    
