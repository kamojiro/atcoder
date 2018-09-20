import heapq
from itertools import accumulate

n, m, s, t = map( int, input().split())

def dijkstra(graph, start):
    dist = [ 10**14 for _ in range(n)]
    dist[start] = 0
    q = [(0,start)]
    while q:
        l, v = heapq.heappop(q)
        if dist[v] < l:
            continue
        for u, d in graph[v].items():
            if dist[u] > l+d:
                dist[u] = l+d
                heapq.heappush(q, (dist[u], u))
    return dist

D_yen = [ dict() for _ in range(n)]
D_snuuk = [ dict() for _ in range(n)]
for _ in range(m):
    u, v, a, b = map( int, input().split())
    u, v = u-1, v-1
    D_yen[u][v] = D_yen[v][u] = a
    D_snuuk[u][v] = D_snuuk[v][u] = b

C_yen = dijkstra(D_yen, s-1)
C_snuuk = dijkstra(D_snuuk, t-1)

ANS = list( accumulate( [y+s for y, s in zip( C_yen, C_snuuk)][::-1], min))
[ print( 10**15 - ANS[i]) for i in range(n-1,-1,-1)]
