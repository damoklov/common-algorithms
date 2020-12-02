from plate import Plate

num_paths = 0


def main():
    maze = read_maze('maze1.txt')
    for l in range(len(maze)):
        check_next(maze, (l, 0))


def read_maze(filename):
    with open(filename, 'r') as f:
        columns, rows = (map(int, f.readline().split(' ')))
        maze = [[None for i in range(columns)] for j in range(rows)]
        for i in range(rows):
            line = f.readline()
            for j in range(columns):
                maze[i][j] = Plate(line[j].strip(), (i, j))
    return maze


def check_exit(maze, index):
    column_top = 0
    column_bottom = len(maze) - 1
    row = len(maze[0]) - 1
    return index == (column_bottom, row) or index == (column_top, row)


def check_next(maze, i):
    global num_paths
    if check_exit(maze, i):
        maze[i[0]][i[1]].is_visited = True
        num_paths += 1
        return maze
    if len(maze) > 1:
        for j in range(0, len(maze)):
            for k in range(i[1] + 1, len(maze[0])):
                if maze[j][k].value == maze[i[0]][i[1]].value and \
                        (j, k) != (i[0] - 1, i[1] + 1) and \
                        (j, k) != (i[0] + 1, i[1] + 1) and \
                        (j, k) != (i[0], i[1] + 1):
                    maze = check_next(maze, (j, k))
        if i[0] - 1 >= 0 and i[1] + 1 < len(maze[0]) and maze[i[0]][i[1]].value == maze[i[0]-1][i[1]+1].value:
            maze = check_next(maze, (i[0] - 1, i[1] + 1))
        if i[1] + 1 < len(maze[0]) and i[0] + 1 < len(maze) and maze[i[0]][i[1]].value == maze[i[0]+1][i[1]+1].value:
            maze = check_next(maze, (i[0] + 1, i[1] + 1))
        if i[1] + 1 < len(maze[0]):
            maze = check_next(maze, (i[0], i[1] + 1))
        maze[i[0]][i[1]].is_visited = True
    else:
        num_paths += 1
        for k in range(i[1] + 1, len(maze[0])):
            if maze[0][k].value == maze[i[0]][i[1]].value and (0, k) != (i[0], i[1] + 1):
                maze = check_next(maze, (0, k))
    return maze


if __name__ == '__main__':
    main()
    print(num_paths)
