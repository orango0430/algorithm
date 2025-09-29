def counting_sort(arr):
    max_arr = max(arr)
    count = [0] * ((max_arr)+1)
    sorted_arr = list()
    for i in arr:
        count[i] += 1
    print(count)
arr = [2,1,2,3,1]
counting_sort(arr)
