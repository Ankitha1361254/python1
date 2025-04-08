count=100

prisons=["C"]*count


for i in range(0,count,1):
    prisons[i]="O"


for i in range(1,count,2):
    prisons[i]="C"

for j in range(2,count,1):
    
    for i in range(j,count,j+1):
        if prisons[i]=="C":
            prisons[i]="O"
        else:
            prisons[i]="C"
    

for i in range(0,count,1):
    if prisons[i]=="O":
        print(i+1,end="\t")
        
