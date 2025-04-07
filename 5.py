def calc1(num1,num2):
    

    
    sum1=num1+num2
    diff=num1-num2
    mul=num1*num2
    div1=num1/num2
    div2=num1//num2
    mod=num1%num2
    exp1=num1**num2
    print(sum1,diff,mul,div1,div2,mod,exp1)

f1=open("in2.txt","r")
s1=f1.readline()
list1=s1.split(",")
num1=int(list1[0])
num2=int(list1[1])
calc1(num1,num2)


