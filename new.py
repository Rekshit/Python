import numpy as np
list1 = [10,11,12,13,14]
list2 = [15,16,17,18,19]

arr1 = np.array(list1)
arr2 = np.array(list2)
print("The elements in array1 are:", arr1)
print("The elements in array2 are:", arr2)

total_sum = arr1 + arr2
print("The sum of arr1 and arr2 is:", total_sum)

sum1 = np.sum(arr1)
print("The sum of arr1 is:", sum1)
sum2 = np.sum(arr2)
print("The sum of arr1 is:", sum2)

total_mul = arr1 * arr2
print("The product of arr1 and arr2 is:", total_mul)

mean_1 = np.mean(arr1)
print("The mean of arr1 is:", mean_1)
mean_2 = np.mean(arr2)
print("The mean of arr2 is:", mean_2)

max_1 = np.max(arr1)
print("The maximum element of arr1 is:", max_1)
max_2 = np.max(arr2)
print("The maximum element of arr2 is:", max_2)