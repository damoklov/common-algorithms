import time
from camera import Camera


def read_from_csv(filename):
    with open(filename, 'r') as f:
        f.readline()
        objects = [Camera(*item) for item in [line.strip().split(',') for line in f.readlines()]]
    return objects


def main():
    objects = read_from_csv('cameras.csv')

    print('========================')
    print('Bubble sort (descending)')
    print('========================')
    start = time.time()
    objects = Camera.bubble_sort_by_memory_size_descending(objects)
    end = time.time() - start
    print("Time spent: " + str(end))
    print("Number of comparisons: " + str(Camera.bubble_sort_comparison_counter))
    print("Number of swaps: " + str(Camera.bubble_sort_swap_counter))
    print('========================')
    [print(object_to_show) for object_to_show in objects]

    print()

    print('======================')
    print('Merge sort (ascending)')
    print('======================')
    start = time.time()
    objects = Camera.merge_sort_zoom_ascending(objects)
    end = time.time() - start
    print("Time spent: " + str(end))
    print("Number of comparisons: " + str(Camera.merge_sort_comparison_counter))
    print("Number of swaps: " + str(Camera.merge_sort_swap_counter))
    print('======================')

    [print(object) for object in objects]


if __name__ == '__main__':
    main()
