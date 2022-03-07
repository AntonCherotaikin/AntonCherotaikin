my_list = [i ** 3 for i in range(1, 1001) if i % 2 != 0]

nums_seven = []
for number in my_list:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seven.append(number)

nums_seven_sum = sum(nums_seven)
print(nums_seven_sum)

added_seventeen = []
for i in my_list:
    new = i + 17
    added_seventeen.append(new)

nums_seventeen_seven = []
for number in added_seventeen:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seventeen_seven.append(number)

nums_seventeen_seven_sum = sum(nums_seventeen_seven)
print(nums_seventeen_seven_sum)