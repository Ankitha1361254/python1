def calc1(num1,num2):
    

    
    sum1=num1+num2
    diff=num1-num2
    mul=num1*num2
    div1=num1/num2
    div2=num1//num2
    mod=num1%num2
    exp1=num1**num2
    print(sum1,diff,mul,div1,div2,mod,exp1)

f1=open("in1.txt","r")
num1=int(f1.readline())
num2=int(f1.readline())
calc1(num1,num2)

