#LIST_DATATYPE

grocery=["Harpic","Vim bar","deodrant",32]
#print(grocery)#All
#print(grocery[2])#specific
numbers=[2,7,9,11,3]
#numbers.sort()#increasing order
#numbers.reverse()#Decreasing order
#numbers.append(71)#add no. to the list at end
#numbers.insert(1,16)#add a no. format(place, no.) to the list
#numbers.remove(7)#remove a no.
#numbers.pop()#last no. will be removed
#numbers[1]=98
#print(numbers)
"""print(numbers[:4])#slicing
print(numbers[::-1])#reversing
print(numbers[1:5:2])
print(len(numbers))#total length
print(max(numbers))#max no.
print(min(numbers))#min no."""
#mutable= can change
#immutable= Can't change
#tp=(1,2,3)#tp=tupple---> It is an immutable function
#print(tp)
"""Interchange a no."""
a=1
b=8
a,b = b,a
#temp=a
#a=b
#b=temp #(traditional way)
print(a,b)