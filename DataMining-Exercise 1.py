
test_str = input("Enter a string: ")
dict = {}
for i in test_str:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1
print(" :\n "
      + str(dict))