
# Problem 1: 2D array: Hourglass Sum

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

# Arrays Problem 2; Left Rotation
# A left rotation operation on an array shifts each of the 
# array's elements 1 unit to the left.

def rotLeft(a, d):
    a_len = len(a)

    def shift(a_len,new_index):
        if new_index >= a_len:
            new_index = new_index - a_len
        return new_index

    return [a[shift(a_len,index+d)] for index, val in enumerate(a)]


# ===================================================
# problem 3: New Year's chaos

# Any person in the queue can bribe the person directly in front of them to swap positions. 
# If two people swap positions, they still wear the same sticker denoting their original places in line. 
# One person can bribe at most two others

# print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible

def minimumBribes(q):
	print(q)
	g = {}
	g_1 = []
	for index, val in enumerate(q):
		if index < val - 1:
			g[index] = val -1
			g_1.append(index+1)
		if val in g_1:
			g[index] = val-1
	print(g)
	print(g_1)

	cycles = set()
	for k, v in g.items():
    		if g.get(v) == k:
        		cycles.add(tuple(sorted((k, v))))
	print(cycles)
	return g

# ==================================================
if __name__ == "__main__":
	minimumBribes([2, 1, 5, 3, 4])
