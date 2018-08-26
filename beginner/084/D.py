prime_list = list(range(2,10**5))
k = 0
prime = []
for Q in prime_list:
    for x in prime_list:
        if x != Q and x%Q == 0:
            prime_list.remove(x)
print(prime_list)
    
