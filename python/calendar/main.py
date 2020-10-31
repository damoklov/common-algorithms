from calendar import Calendar, Node


def main():
    calendar = Calendar()
    new_node = Node((5, 8))
    calendar.insert_into_sorted(new_node)
    new_node = Node((3, 5))
    calendar.insert_into_sorted(new_node)
    new_node = Node((0, 1))
    calendar.insert_into_sorted(new_node)
    new_node = Node((4, 8))
    calendar.insert_into_sorted(new_node)
    new_node = Node((10, 12))
    calendar.insert_into_sorted(new_node)
    new_node = Node((9, 12))
    calendar.insert_into_sorted(new_node)

    print(calendar)
    calendar.optimize()
    print(calendar)


if __name__ == '__main__':
    main()
