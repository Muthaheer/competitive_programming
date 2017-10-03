# cook your dish here

def solution(n):
    ways = [0] * (n+1)
    
    dp = [0] * (n+1)
    
    
    ways[0] = 0
    ways[1] = 1 # for 1 vertex
    ways[2] = 1
    
    # ways[0] = 0
    # ways[1] = 0
    # ways[2] = 1 
    # ways[3] = 2
    
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1

    
    
    for i in range(3, n+1):
        for j in range(1, i):
            ways[i] += ways[j] * ways[i-j]
            
        dp[i] = ways[i-1] + dp[i-1]
        
        for j in range(2, i):
            s = 0
            for k in range(i-j):
                s += dp[i-j-k]
                
            dp[i] += s * (i-j)
        
        # for j in range(2, i):
        #     for k in range(1, j+1):
        #         dp[i] += dp[k] + dp[j+1-k]
        
        
                
                
    #print(ways)
    print(dp[n])
    
solution(5)
                