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
	km={v:k for k,v in mapp.items()}
	print(amount)
	if(sum(amount)!=0):
		print("Not possible to resolve as there would be some problems")
		return
	while True:

		given = amount.index(max(amount))
		taken = amount.index(min(amount))
		found=False
		for i in range(len(amount)):
			temp=amount[i]
			if found:
				break
			for j in range(i+1,len(amount)):
				if temp==amount[j]:
					continue
				elif temp+amount[j]==0 and temp!=0 and amount[j]!=0:
					print( km[i] , " owes " , temp ,"to", km[j])		
					amount[i] -=temp 
					amount[j] += temp 
					found=True
					#splitwise(amount,mapp)
					break
		if (amount[given] == 0 and amount[taken] == 0): 
			break 
		minimum = min(-amount[taken], amount[given]) 
		amount[given] -=minimum 
		amount[taken] += minimum
		print( km[taken] , " owes " , minimum ,"to", km[given]) 
		print("Amount ",amount)
	print("Amount ",amount)
		 

#splitwise([370, -50, - 300,-50, - 40, -30],{"A":0,"B":1,"C":2,"D":3,"E":4,"F":5})


'''
#User input
n=int(input("Enter Number of participants"))
amount=[]
mapp={}
count=0
c='A'
for i in range(n):
	mapp[c]=count
	count=count+1
	c=chr(ord(c)+1)
count=0
km={v:k for k,v in mapp.items()}
for i in range(n):
	amount.append(int(input("Enter Amount for {}\n ".format(km[count]))))
	count=count+1
splitwise(amount,mapp)

'''
