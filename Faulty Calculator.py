#45*3=555,56+9=77,56/6=4
"""Design a calculator which will correctly solve all the problemsexcept the above ones
Your program should take operator and the two numbers as input from the user and then return the result"""
n1=int(input())
n2=int(input())
n=input()
if n1==45 and n2==3 and n=="*":
    print("555")
elif n1==56 and n2==9 and n=="+":
    print("77")
elif n1==56 and n2==6 and n=="/":
    print("4")
else:
    if n=="+":
        print("",n1+n2)
    if n=="-":
     print("",n1-n2)
    if n=="*":
        print("",n1*n2)
    if n=="/":
        print("",n1/n2)
