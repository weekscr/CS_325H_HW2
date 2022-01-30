import numpy
import time
#0-1 Knapsack problem

#recursive
def knapsack_recursive(v,w,n,W):

    if n==0 or W==0:
        return 0    #base case

    if w[n-1] > W:
        return knapsack_recursive(v,w,n-1,W)    #item is too big
    else:
        return max(v[n-1] + knapsack_recursive(v,w,n-1,W-w[n-1]), knapsack_recursive(v,w,n-1,W)) #item can fit and either adds value or doesn't



def knapsack_DP(v,w,n,W):
    V = [[0 for i in range(W+1)] for i in range(n+1)]
    
    for i in range(n + 1):
        for j in range(W + 1):
            
            if i == 0 or j == 0:
                V[i][j] = 0        #set base cases to 0
                
            elif w[i-1] <= j:     #if item fits 
                
                if v[i-1] + V[i-1][j-w[i-1]] > V[i-1][j]:    #item will add overall value
                    
                    V[i][j] = v[i-1] + V[i-1][j-w[i-1]]
                else: 
                    V[i][j] = V[i-1][j]       #item wont add value. Use previous solution
            else:
                V[i][j] = V[i-1][j]   #item wont fit. Use previous solution

    return V[n][W]        


n = [10,15,20,25]
W = [100,200,500]

for i in range(len(W)):
    for j in range(len(n)):
        v = numpy.random.randint(0,100,n[j])
        w = numpy.random.randint(0,20,n[j])

        start=time.time()
        maxRec = knapsack_recursive(v,w,n[j],W[i])
        end=time.time()
        tRec = end-start

        start1=time.time()
        maxDP = knapsack_DP(v,w,n[j],W[i])
        end1=time.time()
        tDP = end1-start1
        
        print("N=",n[j]," W=",W[i]," Rec time = ",'{:.9f}'.format(tRec)," DP time = ",'{:.9f}'.format(tDP)," max Rec = ",maxRec," max DP = ",maxDP)




