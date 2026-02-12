""""nums1 = [2, 4, 6, 0, 0, 0]
m = 3
nums2 = [9, 15, 22]
n = 3

midx = m - 1
nidx = n - 1
right = m + n - 1

while nidx >= 0:
    if midx >= 0 and nums1[midx] > nums2[nidx]:
        nums1[right] = nums1[midx]
        midx -= 1
    else:
        nums1[right] = nums2[nidx]
        nidx -= 1
    right -= 1

print(nums1)
"""

"""def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    return arr3
m = int(input("Enter the number of elements in the first array: "))
n = int(input("Enter the number of elements in the second array: "))
print("Enter",m," elements for the first array separated by spaces:")
arr1 = list(map(int, input().split()))
print("Enter",n," elements for the second array separated by spaces:")
arr2 = list(map(int, input().split()))
if len(arr1) != m or len(arr2) != n:
    print("Invalid")
else:
    arr3 = merge_arrays(arr1, arr2)
    print("Merged and sorted array:")
    for value in arr3:
        print(value, end=" ")"""