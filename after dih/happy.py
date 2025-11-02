t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    m = a == b == c == d
    if m:
        print("YES")
    else:
        print("NO")