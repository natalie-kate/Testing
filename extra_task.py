def add_tuple_lists(*args):
    """ Add together two lists of tuples of integers.

    arguments:
    *args (list): - lists of tuples of integers, all of which have the same
                        length

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in
    list a and list b
    """
    added_tuples = []
    # the for loops are oriented so that we loop through each argument passed
    # in and add the values. we append that value to the list that is created
    # for each tuple, so we end up with a list like you had - each summed value
    # is in the same position as the corresponding tuple values. we then make
    # that into a tuple (again, like yours) and append it to the result. then
    # we create a fresh list and start again for the next tuple in the original
    # lists. make sense?
    if args and args[0]:  # check that non-empty lists have been passed in
        for j in range(len(args[0])):  # for each tuple in the list
            temp_list = []  # create an empty array (similar to your solution)
            for k in range(len(args[0][j])):  # for each value in the tuple
                num = 0
                for i in range(len(args)):  # for each list passed in
                    num += args[i][j][k]
                temp_list.append(num)
            added_tuples.append(tuple(temp_list))

    return(added_tuples)  # I think you know what this does ;P
