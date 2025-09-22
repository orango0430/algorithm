arr = [5,3,9,7,6,4,1,2]
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr = []
    i = h = 0
    while i < len(low_arr) and h < len(high_arr):
        if low_arr[i] < high_arr[h]:
            merged_arr.append(low_arr[i])
            i += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[i:]
    merged_arr += high_arr[h:]
    return merged_arr
print(merge_sort(arr))