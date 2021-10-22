#FOR LOOP
"""list1=(["harry",1],["larry",2],["carry",6],["marie",250])
dict1=dict(list1)
#print(dict1)
for item in dict1:
    print(item)"""

#for item,lollipop in dict1.items():
    #print(item,"and lollipop is",lollipop)

"""list1=[int(input())]
if int(input())>6:
    for item in list1:
        print(list1)"""
items=[int,float,"ashu",5,3,6,7,3,7,8,5,34,23,53]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)