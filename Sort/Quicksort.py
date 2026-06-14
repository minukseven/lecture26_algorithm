import sys
sys.setrecursionlimit(10**6)

class QuickSort:
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
        self.quick_sort(num_list, 0, len(num_list) - 1)
        print(num_list)

    def quick_sort(self, A, left, right):
        if left < right:
            p = self.partition(A, left, right)
            self.quick_sort(A, left, p-1)
            self.quick_sort(A, p+1, right)

    def partition(self, A, left, right):
        pivot = A[left]
        low = left + 1
        high = right
        while low <= high:
            while low <= high and A[low] < pivot: low += 1
            while low <= high and A[high] > pivot: high -= 1
            if low <= high:
                A[low], A[high] = A[high], A[low]
                low += 1
                high -= 1
        A[left], A[high] = A[high], A[left]
        return high

if __name__ == '__main__':
    app = QuickSort()
    app.main()