arr = [None,5,3,9,7,6,4,1,2]
def heapify(A, k, n):
    """
    A[k]를 루트로 하는 부분트리를 최소힙 성질을 만족하도록 만드는 함수
    A : 1-based 배열 (앞에 dummy 값 하나 둬야 함)
    k : 현재 노드 인덱스
    n : 힙 크기 (배열 길이 - 1)
    """
    left = 2 * k
    right = 2 * k + 1

    # 자식 중 더 작은 쪽 찾기
    if right <= n:  # 두 자식 모두 존재
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:  # 왼쪽 자식만 존재
        smaller = left
    else:  # 자식 없음
        return

    # 부모보다 자식이 더 작으면 교환하고 내려보내기
    if A[smaller] < A[k]:
        A[k], A[smaller] = A[smaller], A[k]  # swap
        heapify(A, smaller, n)  # 교환된 자리에서 다시 검사


def build_heap(A):
    """
    배열 A[1..n]을 최소 힙으로 만드는 함수
    """
    n = len(A) - 1  # dummy 제외한 실제 원소 개수
    for i in range(n // 2, 0, -1):  # ⌊n/2⌋ downto 1
        heapify(A, i, n)
build_heap(arr)
print((arr[1:]))