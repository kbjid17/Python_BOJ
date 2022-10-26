import sys

input = sys.stdin.readline

N,T = map(int,input().split())
ar = [[0]*(T+1) for _ in range(N+1)]
test = [[0]*(3) for _ in range(N+1)]
for i in range(N):
  a,b = map(int,input().split())
  test[i][1] = a
  test[i][2] = b

test.sort(key = lambda x:x[1])

for i in range(1,N+1):
  for j in range(1,T+1):
    if(j < test[i][1]):
      ar[i][j] = ar[i-1][j]
    else:
      ar[i][j] = max(ar[i-1][j],ar[i-1][j-test[i][1]] + test[i][2])

print(ar[N][T])