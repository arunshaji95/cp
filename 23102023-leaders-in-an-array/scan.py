# Write a program to print all the LEADERS in the array. 
# An element is a leader if it is greater than all the elements to its right side. 
# And the rightmost element is always a leader. 
# Time complexity is O(n)

input_array = [16, 17, 4, 3, 5, 2]
maximum = 0
stack = []
for i in range(len(input_array)-1, -1, -1):
    if input_array[i] > maximum:
        stack.append(input_array[i])
    maximum += input_array[i]
while stack:
    print(stack.pop(), end=",")
print()