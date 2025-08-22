x,y = map(int,input().split())
sum = 0
for i in range(1 , x+1):
    sum = sum + (1<<(x+y-i))

print(sum)