# Python3 code to demonstrate working of
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()

# initializing list
test_list1 = ['idtest','idtest2', 'idtest3']
test_list2 = ['ratings', 'price', 'score']

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()
res = [{a: {b}} for (a, b) in zip(test_list1, test_list2)]

# printing result
print("The constructed dictionary : " + str(res))

