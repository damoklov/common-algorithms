class Camera:
    bubble_sort_comparison_counter = 0
    bubble_sort_swap_counter = 0
    merge_sort_comparison_counter = 0
    merge_sort_swap_counter = 0

    def __init__(self, manufacturer, memory_size, zoom):
        self.manufacturer = manufacturer
        self.memory_size = memory_size
        self.zoom = zoom

    def __str__(self):
        return (self.__class__.__name__ +
                '('
                + ','.join([self.manufacturer, self.memory_size, self.zoom]) +
                ')')

    @staticmethod
    def bubble_sort_by_memory_size_descending(objects):
        n = len(objects)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if objects[j].memory_size < objects[j + 1].memory_size:
                    Camera.bubble_sort_comparison_counter  += 1
                    objects[j].memory_size, objects[j + 1].memory_size = \
                        objects[j + 1].memory_size, objects[j].memory_size
                    Camera.bubble_sort_swap_counter += 2
        return objects

    @staticmethod
    def merge_sort_zoom_ascending(objects):
        if len(objects) > 1:
            mid = len(objects) // 2
            left_part = objects[:mid]
            right_part = objects[mid:]

            Camera.merge_sort_zoom_ascending(left_part)
            Camera.merge_sort_zoom_ascending(right_part)

            i = j = k = 0

            while i < len(left_part) and j < len(right_part):
                Camera.merge_sort_comparison_counter += 2
                if left_part[i].zoom < right_part[j].zoom:
                    Camera.merge_sort_comparison_counter += 1
                    objects[k] = left_part[i]
                    i += 1
                else:
                    objects[k] = right_part[j]
                    j += 1
                k += 1

            while i < len(left_part):
                Camera.merge_sort_comparison_counter += 1
                objects[k] = left_part[i]
                i += 1
                k += 1

            while j < len(right_part):
                Camera.merge_sort_comparison_counter += 2
                objects[k] = right_part[j]
                j += 1
                k += 1
        return objects
