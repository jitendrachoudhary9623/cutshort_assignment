import numpy as np
from cutshort import *
array=[{ 	"paidBy": "A", 	"paidFor": { "B": 100, "C": 50 } 	},{ 	"paidBy": "A", 	"paidFor": { "C": 500 } 	},{ 	"paidBy": "B", 	"paidFor": { "A": 150, "C": 200 }},{ 	"paidBy": "C", 	"paidFor": { "A": 200, "B": 200 } 	},{ 	"paidBy": "D", 	"paidFor": { "A": 350 } 	},{ 	"paidBy": "E", 	"paidFor": { "D": 250,"B":50 } 	}]
print(array)

#calculates no of participants
participants=set()
for t in array:
	participants.add(t["paidBy"])
noOfParticipants=len(participants)
pTracker={}
count=0
for p in participants:
	pTracker[p]=count
	count=count+1
print(participants,pTracker)

inputArray=np.zeros(shape=(noOfParticipants,noOfParticipants))
print(inputArray)

for t in array:
	for key,value in t["paidFor"].items():
		inputArray[pTracker[t["paidBy"]]][pTracker[key]]=inputArray[pTracker[t["paidBy"]]][pTracker[key]]+value

print(inputArray)
output(inputArray,noOfParticipants,pTracker) 
