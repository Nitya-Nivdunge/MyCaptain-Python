num=int(input("Enter the number of elements of the list : "))
inp_list=[]
opt_list=[]
print("Enter the elements : ")

# To take input of elements of list from the user
while  num-1 >= len(inp_list):
    inp_list.append(int(input()))

print("\nPositive elements of the list are : ")
print("\nInput List : ",inp_list)

# To seperate positive elements of the list and add it to another list
for i in inp_list:
    if i>=0:
        opt_list.append(i)
    
print("Output     : ",opt_list)
