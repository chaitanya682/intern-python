dict1={"name":"Hemavarshini","age":21,"clg":"svce"}
dict2={"name1":"friends","age1":20,"clg1":"REC","year":2020}
newdict=dict1.copy()
for key,value in dict2.items():
    newdict[key]=value
print(newdict)

del newdict["age"]
#also newdict.pop("age")

#map 2 lists in a dict
list1=["a","b","c","d"]
list2=["e","f","g","h"]
dict5=dict(zip(list1,list2))
print(dict5)

#len of a set

set={1,2,3,4,5,6,3,33,32}
print("the length of the set is : ", len(set))

#remove set intersection

set1={1,2,3,4,5,6,7,8,9}
set2={2,12,13,11,14,15,5}
z=set1-set2
print(z)