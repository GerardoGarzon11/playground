# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# create blank list
mylist2 = list()
print(mylist2)

# get item
item = mylist[0]
print(item)

# loop list
for i in mylist:
    print(i)

# check if value is in list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# insert at the end
mylist.append("lemon")
print(mylist)

# insert at specific index
mylist.insert(2, "blueberry")
print(mylist)

# remove last item (returns it)
item = mylist.pop()
print(item)
print(mylist)

# remove a specific item, throws error if item is not present
item = mylist.remove("banana")
print(mylist)

# remove all elements
# mylist.clear()

# sort list
new_list = sorted(mylist)
print(new_list)

# sort list in-place
mylist.sort()
print(mylist)

mylist = [0] * 5
print(mylist)

# Concatenation
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

# slicing with steps
a = mylist[::2]
print(a)

# reversing
b = mylist[::-1]
print(b)

# copying
list_original = ["banana", "cherry", "apple"]

# copies, but has both list are the same
list_copy = list_original

print(list_copy)

list_copy.append("pear")
print(list_copy)
print(list_original)

# copying without having reference to original
list_copy = list_original.copy()
list_copy = list(list_original)
list_copy = list_original[:]

# list comprehensions
a = [1, 2, 3, 4, 5, 6]
b = [elem * elem for elem in a]
print(a)
print(b)
