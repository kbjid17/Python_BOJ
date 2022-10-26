import sys

input = sys.stdin.readline

N,M,V = map(int,input().split())

visited = [0] * (N+1)
ar = [[0]*(N+1) for _ in range(N+1)]

queue = [V]
for i in range (M):
  a,b = map(int,input().split())
  ar[a][b] = 1
  ar[b][a] = 1

queue_list = []
visited[V] = 1

while queue:
  q = queue.pop(0)
  queue_list.append(q)
  for i in range (1,N+1):
    if(ar[q][i] == 1 and visited[i] == 0):
      queue.append(i)
      visited[i] = 1


visited = [0] * (N+1)
stack_list = []

def dfs(V):
  stack = [V]
  visited[V] = 1
  stack_list.append(V)
  while stack:
    s = stack.pop(0)
    for i in range(1,N+1):
      if(ar[s][i] == 1 and visited[i] == 0):
        stack.append(i)
        visited[i] = 1
        dfs(i)

dfs(V)
for i in stack_list:
  print(i,end = " ")
print()

for i in queue_list:
  print(i, end = " ")