from math import ceil
N = int( input())
bridge, blue = map( int, input().split())
for _ in range(N-1):
    t, a = map( int, input().split())
    tbridge = (bridge//t+ceil(bridge%t))*t
    tblue = (bridge//t+ceil(bridge%t))*a
    abridge = (blue//a+ceil(blue%a))*t
    ablue  = (blue//a+ceil(blue%a))*a
    if tbridge - bridge < 0 or tblue - blue < 0:
        bridge = abridge
        blue = ablue
    elif abridge - bridge < 0 or ablue - blue < 0:
        bridge = tbridge
        blue = tblue
    elif abridge + ablue < tbridge + tblue:
        bridge = abridge
        blue = ablue
    else:
        bridge = tbridge
        blue = tblue
    # if (bridge//t+ceil(bridge%t))*a > blue:
    #     bridge = (bridge//t+ceil(bridge%t))*t
    #     blue =  (bridge//t+ceil(bridge%t))*a
    # else:
    #     blue = (blue//a+ceil(blue%a))*a
    #     bridge = (blue//a+ceil(blue%a))*t
    print( bridge, blue)
print( bridge + blue)
