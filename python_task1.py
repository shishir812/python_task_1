two_pair_values = [
    [1, 5],
    [9, -7],
    [0, 8],
    [6, 3],
    [4, 11],
    [14, 0],
    [8, 1],
    [4, 9],
]
target_value = 9

def get_aspected_index(two_pair_values, target_value):


    for i in two_pair_values:
        for j in i:
            j = i[0] + i[1]
#            print(j)
#            break
        if ((j == target_value) and (i[1] == 1)):
            print("Index of Target value:", two_pair_values.index(i))



get_aspected_index(two_pair_values, target_value)
