# Write a program to print all the LEADERS in the array. 
# An element is a leader if it is greater than all the elements to its right side. 
# And the rightmost element is always a leader. 
# Time Complexity O(n^2)
leaders = []
input_array = [1, 2, 3, 4, 5, 2]
for  i, item in enumerate(input_array):
    flag = True
    for  j, sub_element in enumerate(input_array[i+1:]):
        if item < sub_element:
            flag = False
            break
    if flag:
        leaders.append(item)
print(leaders)
