def table1(n1,n2):
    for j in range(n1,n2+1,1):
        
        for i in range(1,11,1):
            print(j,i,j*i)
        print()

f1=open("in3.txt","r")
s1=f1.readline()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
table1(n1,n2)



