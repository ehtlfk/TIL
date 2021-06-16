def permutation(n,k):
    if n == k:
        print(ret)
        return
    else:
        for i in range(len(numbers)):
            if visited[i] == 0:
                visited[i] = 1 # 중복 차단
                ret[k] = numbers[i]
                permutation(n,k+1)
                visited[i] = 0
            
n = 5
r = 3
numbers = list(range(1,n+1))
visited = [0]*n
ret = [0]*r
permutation(r,0)
