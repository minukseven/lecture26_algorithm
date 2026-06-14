import sys
sys.setrecursionlimit(10**6)

class MergeSort:
    def main(self):
        num_list = []
        while True:
            try:
                input_num = int(input('정렬할 숫자 입력(입력종료=0): '))
            except ValueError:
                print('숫자만 입력하세요')
            else:
                if input_num == 0:
                    break
                num_list.append(input_num)
        self.merge_sort(num_list, 0, len(num_list) - 1)
        print(num_list)

    def merge_sort(self, A, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(A, left, mid)
            self.merge_sort(A, mid + 1, right)
            self.merge(A, left, mid, right)

    def merge(self, A, left, mid, right):
        sorted_arr = [0] * len(A)
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if A[i] <= A[j]:
                sorted_arr[k] = A[i]
                i += 1
            else:
                sorted_arr[k] = A[j]
                j += 1
            k += 1

        if i > mid:
            sorted_arr[k:right+1] = A[j:right+1]
        else:
            sorted_arr[k:right+1] = A[i:mid+1]

        A[left:right+1] = sorted_arr[left:right+1]

if __name__ == '__main__':
    app = MergeSort()
    app.main()