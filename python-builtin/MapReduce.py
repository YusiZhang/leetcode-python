if __name__ == '__main__':
    # map() can be applied to more than one list.
    # The lists have to have the same length.
    # map() will apply its lambda function to the elements of the argument lists,
    # i.e. it first applies to the elements with the 0th index,
    # then to the elements with the 1st index until the n-th index is reached:

    # var_map is a list where [1+4, 2+5, 3+6]
    var_map = map(lambda x,y: x+y, [1,2,3],[4,5,6])
    print var_map

    # The function reduce(func, seq) continually applies the function func() to the sequence seq.
    # It returns a single value.

    # var_reduce is a single value where 1+2+3
    var_reduce = reduce(lambda x,y: x+y, [1,2,3])
    print var_reduce