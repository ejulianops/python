def row_sums(my_matrix: list):

    for line in my_matrix:
        sum_list = sum(line)
        line.append(sum_list)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
