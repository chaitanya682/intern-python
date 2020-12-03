n=int(input("Enter the number of values: "))
Benito_list=[]
for count_inp in range(0,n):
    inp=int(input("Enter a number: "))
    Benito_list.append(inp)

print("The List: ")
print(Benito_list)
Benito_list.append("thomas")
print("The List after append:",Benito_list)
Benito_list.pop()
print("The list after deleting an item :", Benito_list)
max_num=max(Benito_list)
print(max_num)
min_num=min(Benito_list)
print(min_num)