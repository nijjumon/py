#set is an array(same data type) with no repition of items (will filter out repitions automatically blyat cyka)

s1=set(["raju", "satish", "keshav", "payal", "satish"])
print(s1)
s2=set(["raju","mau bakhro"])
print(s2)




u=s1.union(s2)
print(u)
print(s1.intersection(s2))

#immutable
s3=frozenset(["raju"])
print(s3)
s3=set(["raju", "rastogi"])
print(s3)

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
print(vowels)
print(vowels)
fSet = frozenset(['a', 'e', 'i', 'o', 'u'])
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
print('The frozen set is:', fSet)
print('The frozen set is:', fSet)