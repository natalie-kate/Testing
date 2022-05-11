def add_tuple_lists(list_a, list_b):
    """ Add together two lists of tuples of integers.

    Keyword arguments:
    list_a -- a list of tuples of integers, all of which have the same length
    list_b -- another list of tuples of integers, which have the same length as list_a

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in list a and list b
    """

    # Oh dear, there's nothing here!

    
    # My crap solution
    """def add_tuple_lists(list_a, list_b):
        new_list = []
        for i in range(0, len(list_a)):
            new_tuple = []
            for n in range(0, len(list_a[i])):
                new_int = list_a[i][n] + list_b[i][n]
                new_tuple.append(new_int)
            new_list.append(tuple(new_tuple))
        return new_list"""