from functions_and_modules import arithemetic
#
#
# a=input("enter a no.")  #input taken in a is vague  i.e has no defined data type
# b=int(a)                #in this line we have used b to represent integer of a
# if b>0:
#     print("+ve")
# elif b<0:
#     print("-ve")
# else:
#     print("neutral")

q=input()
print(type(q))
q=int(q)#important step bitch
w=input()
w=int(w)
add_result = arithemetic.add(q,w)
print(add_result)


