#DICTIONARY:It is nothing but key value pairs
d1={}
#print(type(d1))
d2={"harry":"burger","rohan":"fish","ashu":"roti",
   "subham":{"b":"maggie","l":"rice","d":"chicken"}}
"""print(d2["harry"])
print(d2["subham"])
print(d2["subham"]["b"])
d2["ankit"]="junk food"
d2[420]="Kababs"
del d2[420]#remove"""
d3=d2.copy()
del d3["harry"]
print(d3)
print(d2.get("harry"))
d2.update({"leena":"toffee"})
print(d2.keys())
print(d2.items())


