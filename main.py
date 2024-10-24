def DE(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] -= 1
    return list
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(DE(nums))
