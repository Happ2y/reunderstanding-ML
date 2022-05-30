'''
    Xn+1 = Xn - n*(df/dx)
    Let y = (x+5)^2
'''


def df(x):
    # returns derivative value
    return 2 * (x+5)


# driver code
if __name__ == "__main__":

    # define learning rate & initial coordinate
    n = 0.01
    curr_X = 3

    # define closeness & maximum iterations
    closeness = 0.000001
    curr_closeness = 1
    max_iterations = 10000
    count_iterations = 0

    # calculate next nearest coordinate & find current closeness
    # when the closeness lowers by 'closeness' or number of iterations exceeds naximum numbers, exit the loop
    while curr_closeness > closeness and max_iterations > count_iterations:
        prev_X = curr_X
        curr_X = curr_X - n * (df(curr_X))
        curr_closeness = abs(prev_X - curr_X)
        count_iterations += 1
        print(f"Iteration : {count_iterations}")
        print(f"X value : {curr_X}")

    print(curr_X)
