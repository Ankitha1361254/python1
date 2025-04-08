count=100
prisons=["C"]*count
lucky=[]

for j in range(0,count,1):
    for i in range(j,count,j+1):
        if prisons[i]=="C":
            prisons[i]="O"
        else:
            prisons[i]="C"
    

for i in range(0,count,1):
    if prisons[i]=="O":
        lucky.append(i+1)
print(lucky)
        
