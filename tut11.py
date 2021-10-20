#SET
s=set()
#s_from_list=set([1,2,3,4])
#print(s_from_list)
#s.add(1)
#s.add(1)
#print(s)
"""s.add(1)
s.add(2)
s1=s.union({1,2,3})
print(s,s1)
s.add(1)
s.add(2)
s1=s.intersection({1,2,3})
print(s,s1)
s.add(1)
s.add(2)
s1={4,6}
print(s.isdisjoint(s1))
s.add(1)
s.add(2)
s.remove(2)
print(s)"""
# import modules
from matplotlib_venn import venn2
from matplotlib import pyplot as plt

# depict venn diagram
venn2(subsets = (50, 10, 7), set_labels = ('Group A', 'Group B'))
plt.show()

