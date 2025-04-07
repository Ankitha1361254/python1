prisons=["C","C","C","C","C","C","C","C","C","C"]
print(prisons)

for i in range(0,10,1):
    prisons[i]="O"
print(prisons)

for i in range(1,10,2):
    prisons[i]="C"
print(prisons)
for j in range(2,5,1):
    
    for i in range(j,10,j+1):
        if prisons[i]=="C":
            prisons[i]="O"
        else:
            prisons[i]="C"
    print(prisons)

