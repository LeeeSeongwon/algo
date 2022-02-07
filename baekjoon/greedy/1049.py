n, m = map(int, input().split())
bund = []
rest = []

for i in range(m):
    b, r = map(int, input().split())
    bund.append(b)
    rest.append(r)
    
ans = 0
bund.sort()
rest.sort()
if bund[0]<=rest[0]*6:
    if bund[0] > rest[0] * (n%6):
        ans = bund[0] * (n//6) + rest[0] * (n%6)
    else:
        ans = bund[0] * (n//6 + 1)
    
else:
    ans = rest[0] * n
print(ans)