input_array = [16, 17, 4, 3, 5, 2]
maximum = 0
for i in range(len(input_array)-1, -1, -1):
    if input_array[i] > maximum:
        print(input_array[i])
    maximum += input_array[i]
