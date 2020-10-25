class Camera:
    bubble_sort_comparison_counter = 0
    bubble_sort_swap_counter = 0
    merge_sort_comparison_counter = 0
    merge_sort_swap_counter = 0

    def __init__(self, manufacturer, memory_size, zoom):
        self.manufacturer = str(manufacturer)
        self.memory_size = int(memory_size)
        self.zoom = float(zoom)

    def __str__(self):
        return (self.__class__.__name__ +
                '('
                + ','.join(list(map(str, [self.manufacturer, self.memory_size, self.zoom]))) +
                ')')

    @staticmethod
    def bubble_sort_by_memory_size_descending(objects):
        n = len(objects)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if objects[j].memory_size < objects[j + 1].memory_size:
                    Camera.bubble_sort_comparison_counter += 1
                    objects[j], objects[j + 1] = objects[j + 1], objects[j]
                    Camera.bubble_sort_swap_counter += 2
                    print([object.memory_size for object in objects])
        return objects

    @staticmethod
    def merge_sort_zoom_ascending(objects):
        if len(objects) > 1:
            mid = len(objects) // 2
            left_part = objects[:mid]
            right_part = objects[mid:]

            left_part = Camera.merge_sort_zoom_ascending(left_part)
            right_part = Camera.merge_sort_zoom_ascending(right_part)

            left_part_iterator = 0
            right_part_iterator = 0
            complete_list_counter = 0

            while left_part_iterator < len(left_part) and right_part_iterator < len(right_part):
                Camera.merge_sort_comparison_counter += 2
                if left_part[left_part_iterator].zoom < right_part[right_part_iterator].zoom:
                    Camera.merge_sort_comparison_counter += 1
                    objects[complete_list_counter] = left_part[left_part_iterator]
                    left_part_iterator += 1
                else:
                    objects[complete_list_counter] = right_part[right_part_iterator]
                    right_part_iterator += 1
                complete_list_counter += 1

            Camera.merge_sort_comparison_counter += 2

            while left_part_iterator < len(left_part):
                Camera.merge_sort_comparison_counter += 1
                objects[complete_list_counter] = left_part[left_part_iterator]
                left_part_iterator += 1
                complete_list_counter += 1

            while right_part_iterator < len(right_part):
                Camera.merge_sort_comparison_counter += 1
                objects[complete_list_counter] = right_part[right_part_iterator]
                right_part_iterator += 1
                complete_list_counter += 1

            Camera.merge_sort_comparison_counter += 2
        return objects
