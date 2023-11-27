def timSort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertionSort(arr, i, min((i + min_run - 1), (n - 1)))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged = merge(arr, start, mid, end)
            arr[start:start + len(merged)] = merged

        size *= 2

    return arr

def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    left_cursor, right_cursor = 0, 0
    merged = []

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    merged += left[left_cursor:]
    merged += right[right_cursor:]

    return merged