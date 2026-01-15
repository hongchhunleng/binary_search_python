my_list=[7,9,12,4,8,3,11]
# step1
min_val=my_list[0]
# step2
for val in my_list:
    if val < min_val:
        min_val = val


print(f"Min value = {min_val}")
