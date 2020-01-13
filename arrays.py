
#TODO Problem 1: 2D array: Hourglass Sum 

def hourglassSum(arr):

    length = len(arr)
    height = len(arr[0])

    def sum_hourglass(m):
        outer_sum = sum(m[0]) + sum(m[2])
        inner_sum = m[1][1]
        return outer_sum + inner_sum

    def transpose(data):
        data_t = [[row[i] for row in data] for i in range(len(data[0]))]
        return data_t

    counter = 0
    max_sum = None

    while counter < length-2:
        sub_matrix = transpose(arr[counter:3+counter])

        for h in range(height-2):
            sub_matrix_t = transpose(sub_matrix[h:h+3])

            temp_max = sum_hourglass(sub_matrix_t)


            if max_sum is None:
                max_sum = temp_max

            else:
                if temp_max > max_sum:
                    max_sum = temp_max

        counter += 1

    return(max_sum)

#? ===========================================

#TODO Arrays Problem 2; Left Rotation
#TODO A left rotation operation on an array shifts each of the 
#TODO array's elements 1 unit to the left.

def rotLeft(a, d):
    a_len = len(a)

    def shift(a_len,new_index):
        if new_index >= a_len:
            new_index = new_index - a_len
        return new_index

    return [a[shift(a_len,index+d)] for index, val in enumerate(a)]


# ===================================================

if __name__ == "__main__":

    # hour glass sum
    # x = [[-9, -9, -9,  1, 1, 1],
    # [ 0, -9,  0,  4, 3, 2],
    # [-9, -9, -9,  1, 2, 3],
    # [0,  0,  8,  6, 6, 0],
    # [0,  0,  0, -2, 0, 0],
    # [0,  0,  1,  2, 4, 0]]
    # print(hourglassSum(x))

    # rot left
    # x = [1,2,3,4,5]
	# d = 2
	# print(rotLeft(x,d))






