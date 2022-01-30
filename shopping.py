
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

    maxV = V[n][W]

    itemNums = []
    #get traceback values
    i=n
    k=W
    while i>0:
        if V[i][k] != V[i-1][k]:
            itemNums.append(i)   #item included
            
            i=i-1
            k=k-w[i]
        else:
            i=i-1      #item not included

    return maxV, itemNums



def shopping(N,P,W,F,M):

    totalPrice = 0
    famArray = [[]]*F
    
    for i in range(F):   #for each family member, run the knapsack problem
        indPrice, indItems = knapsack_DP(P,W,N,M[i])
        totalPrice = totalPrice + indPrice
        famArray[i] = indItems

    return totalPrice, famArray  #sum and return totals
        


f = open('shopping.txt','r').readlines()

T = int(f.pop(0))

for i in range(T):
    N = int(f.pop(0))
    P = [0]*N
    W = [0]*N
    
    for j in range(N):
        temp = f.pop(0)
        temp = temp.split()
        P[j] = int(temp[0])
        W[j] = int(temp[1])

    F = int(f.pop(0))
    M = [0]*F
    
    for j in range(F):
        M[j] = int(f.pop(0))
        
        
    print("Test Case:",i+1)
    tp,fArr = shopping(N,P,W,F,M)
    
    print("Total Price", tp)
    for i in range(F):
        print(str(i+1),end=": ")
        for j in range(len(fArr[i])-1,-1,-1):
            print(fArr[i][j],end=' ')
        print("")
    
