# Task 1

def bubble_sort(list):
    n = len(list)
    left = 0
    right = n - 1
    while left < right:
        # вгору
        for i in range(left, right):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        right -= 1

        # вниз
        for i in range(right, left, -1):
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
        left += 1

    return list


test_list = [15, 10, 20.5, 3, 11]
bubble_sort(test_list)
print(test_list)
# доречно для невеликої кількості данних


# Task 2

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort([15, 10, 20.5, 3, 11]))


# Task 3

def quicksort(arr, threshold=10):
    if len(arr) <= 1:
        return arr

    if len(arr) <= threshold:
        return insertion_sort(arr)

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(quicksort([15, 10, 20.5, 3, 11]))
