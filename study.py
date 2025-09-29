from collections import deque
def radix_sort(arr):
    max_val = max(arr) # 가장 큰 숫자를 찾아 최대 자릿수 계산
    exp = 1 # 자리수를 의미하는 변수, 초기값은 1(1의자리)
    # 최대 자리수만큼 정렬 반복
    while max_val // exp > 0:
    # 0 ~ 9 까지의 큐 리스트 생성
        buckets = [deque() for _ in range(10)]
        # 현재 자리숫에따라 버킷 재배분
        for num in arr:
            index = (num // exp) % 10 # 현재 자릿수에 해당하는 숫자 추출
            buckets[index].append(num) # 해당 숫자에 맞는 버킷 추가
        i = 0 # 버킷에 담긴 데이터를 차례대로 배열에 다시 저장
        for bucket in buckets:
            while bucket:
                arr[i] = bucket.popleft() # 버킷에서 데이터를 꺼내 저장
                i += 1
        exp *= 10 # 다음자리수로 이동
arr = [170,45,75,90,802,24,2,66]
radix_sort(arr)
print("정렬된배열",arr)