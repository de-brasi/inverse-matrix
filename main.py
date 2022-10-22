# Cofactor A_ij = pow(-1, i+j) * det(Submatrix_ij)
# det(Submatrix_ij) is minor

def init_matrix(size_) -> list:
    result_matrix = [[0 for _ in range(size_)]
                     for _ in range(size_)]
    return result_matrix


def get_square_matrix(m_size: int) -> list:
    # matrix is list of rows
    result_matrix = init_matrix(m_size)
    print("Get me matrix values by row")
    for row_idx in range(m_size):
        cur_row_values = [int(x) for
                          x in input().split()]
        assert len(cur_row_values) == m_size
        for col_idx in range(m_size):
            result_matrix[row_idx][col_idx] = \
                cur_row_values[col_idx]

    return result_matrix


def get_determinant(matrix_: len) -> int:
    matrix_size = len(matrix_)
    if matrix_size == 2:
        return matrix_[0][0]*matrix_[1][1]\
               - matrix_[1][0]*matrix_[0][1]
    determinant_ = 0
    row_idx = 0

    for col_idx in range(matrix_size):
        cur_value = matrix_[row_idx][col_idx]
        minor_ = get_submatrix(
                matrix_, row_idx, col_idx)
        minor_sign_ = pow(-1, row_idx + col_idx)
        cofactor_ = minor_sign_ * get_determinant(minor_)
        determinant_ += cur_value * cofactor_

    return determinant_


def get_submatrix(matrix_, row_idx, col_idx) -> list:
    matrix_size = len(matrix_)
    assert matrix_size > 1
    submatrix_ = list()

    for row in range(matrix_size):
        if row == row_idx:
            continue
        cur_row = list()
        for col in range(matrix_size):
            if col != col_idx:
                cur_row.append(matrix_[row][col])
        submatrix_.append(cur_row)

    return submatrix_


def transpone_matrix(matrix_) -> list:
    matrix_size = len(matrix_)
    transponed_matrix = init_matrix(matrix_size)
    for row_idx in range(matrix_size):
        for col_idx in range(matrix_size):
            transponed_matrix[row_idx][col_idx] =\
                matrix_[col_idx][row_idx]
    return transponed_matrix


def get_invertible_matrix(matrix_) -> tuple:
    """
    :param matrix_:
    :return: pair(determinant, matrix_of_cofactor)
    """
    matrix_determinant = get_determinant(matrix_)
    if matrix_determinant == 0:
        return tuple([matrix_determinant, list()])

    matrix_size = len(matrix_)
    matrix_of_cofactor = init_matrix(matrix_size)

    for row_idx in range(matrix_size):
        for col_idx in range(matrix_size):
            # TODO: print founded submatrix
            submatrix_ = get_submatrix(matrix_, row_idx, col_idx)
            print(f"\tFor submatrix (without row={row_idx} and col={col_idx}):")
            print_matrix(submatrix_, 1)

            minor_ = get_determinant(submatrix_)
            minor_sign_ = pow(-1, row_idx + col_idx)
            matrix_of_cofactor[row_idx][col_idx] = minor_sign_ * minor_
            print(f"\tminor multiplier is {minor_sign_}")
            print(f"\tdeterminant is {minor_}")
            print()

    return matrix_determinant, transpone_matrix(matrix_of_cofactor)


def print_matrix(matrix_, offset_=0) -> None:
    max_value_len = max(len(str(i)) for i in sum(matrix_, [])) + 1
    offset_str = '\t' * offset_
    row_line = '+' + ('-'*max_value_len + '+') * len(matrix_)
    for cur_row in matrix_:
        print(offset_str + row_line)
        print(offset_str + '|', end='')
        for el in cur_row:
            # print(offset_str, end='')
            print("{number:>{width}}".format(number=el, width=max_value_len) +
                  '|', end='')
        print()
    print(offset_str + row_line)


def print_invertible_matrix_with_text(matrix_, matrix_multiplier_) -> None:
    print("Invertible matrix is:")
    print_matrix(matrix_)

    if matrix_multiplier_ != 1:
        print(f"With multiplier 1/{determinant}")
    return


print("Get me matrix size: ", end='')
mtrx_size = int(input())
matrix = get_square_matrix(mtrx_size)
print("Source matrix is:")
print_matrix(matrix)
print()
determinant, inv_matrix = get_invertible_matrix(matrix)

print_invertible_matrix_with_text(inv_matrix, determinant)

# TODO: check if source * invertible is singular