'''
    Xn+1 = Xn - n*(df/dx)
    Let y = x^2 + 2y^2
'''


def df_X(x):
    # returns x derivative value
    return 2 * x


def df_Y(y):
    # returns y derivative value
    return 4 * y


# driver code
if __name__ == "__main__":

    # define learning rate & initial coordinate
    n = 0.01
    curr_coord = [3, 4]

    # define closeness & maximum iterations
    closeness = 0.000001
    curr_X_closeness = curr_Y_closeness = 1
    max_iterations = 10000
    count_iterations = 0

    # calculate next nearest coordinate & find current closeness
    # when the closeness lowers by 'closeness' or number of iterations exceeds naximum numbers, exit the loop
    while curr_X_closeness > closeness and curr_Y_closeness > closeness and max_iterations > count_iterations:
        prev_X, prev_Y = curr_coord
        curr_coord[0] = curr_coord[0] - n * (df_X(curr_coord[0]))
        curr_coord[1] = curr_coord[1] - n * (df_Y(curr_coord[1]))
        curr_X_closeness = abs(prev_X - curr_coord[0])
        curr_Y_closeness = abs(prev_Y - curr_coord[1])
        count_iterations += 1
        print(f"Iteration : {count_iterations}")
        print(f"X value : {curr_coord[0]}")
        print(f"Y value : {curr_coord[1]}")

    print(curr_coord[0])
    print(curr_coord[1])
