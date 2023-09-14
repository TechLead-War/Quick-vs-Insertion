import random
import time
import os
import sys

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_runtime(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time


def append_runtime_to_file(filename, runtime, is_float=1):
    algos = ["Array size", "bubble_time", "insertion_time", "quick_time"]
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            for algo in algos:
                file.write(f'{algo}\t')
            file.write(f'\n')
            
    with open(filename, 'a') as file:
        if is_float:
            file.write(f'{runtime:.6f}\t')
            return
        file.write(f'{runtime}\t\t')
        


def append_new_line_to_file(filename):
    with open(filename, 'a') as file:
        file.write('\n')

array_size = 0
def main():
    filename = 'sorting_runtimes.txt'

    arr = generate_random_array(array_size)

    bubble_time = measure_runtime(bubble_sort, arr)
    insertion_time = measure_runtime(insertion_sort, arr)
    quick_time = measure_runtime(quick_sort, arr)

    append_runtime_to_file(filename, array_size, 0)
    append_runtime_to_file(filename, bubble_time)
    append_runtime_to_file(filename, insertion_time)
    append_runtime_to_file(filename, quick_time)
    append_new_line_to_file(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        array_size = int(sys.argv[1])
    else:
        array_size = 1000 # default size if argument not passed
    for i in range(5):
        main()
