N = int( input())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
a,b = 0,0
for i in range(N):
    a ^= A[i]
    b ^= B[i]
print(a)
print(b)
print(a&b)
