def output(array,noOfParticipants,mapp):
    amount = [0 for i in range(noOfParticipants)] 
    #calculate total gain
    for i in range(noOfParticipants): 
        for j in range(noOfParticipants):
        	amount[i] += (array[i][j]-array[j][i])
        	print("Amount",amount)
    #decide how much to give
    splitwise(amount,mapp) 

def splitwise(amount,mapp): 
    given = amount.index(max(amount))
    taken = amount.index(min(amount)) 
    km={v:k for k,v in mapp.items()}
	#prevent recursion
    if (amount[given] == 0 and amount[taken] == 0): 
        return 0 
    minimum = min(-amount[taken], amount[given]) 
    amount[given] -=minimum 
    amount[taken] += minimum
    print(mapp)
    print( km[taken] , " owes " , minimum ,"to", km[given]) 
    print("Amount ",amount)
    splitwise(amount,mapp) 
    
    

