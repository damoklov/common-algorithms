from career import Career


if __name__ == '__main__':
    career = Career('graph.txt')
    print(career.find_optimal_path())
