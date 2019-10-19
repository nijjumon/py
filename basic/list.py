l1=[]
l2=["raju", "shyam", "baburao"]
l3=[l2,["hera", "pheri"]]
print(l2[2])
print(l3[0][1])
l3[1].append("3")



l_temp=["phir"]
l3[1]=l_temp+l3[1]
print(l3)
 # to pop from stack of list
l3=l3.pop()
print("popped value:", l3)
print(l3)
print(type(l3))