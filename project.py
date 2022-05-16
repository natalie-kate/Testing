def add_tuple_lists(list_a, list_b):
    """ Add together two lists of tuples of integers.

    Keyword arguments:
    list_a (list): - a list of tuples of integers, all of which have the same
                        length
    list_b (list): - another list of tuples of integers, which have the same
                        length as list_a

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in
        list a and list b
    """
    added_tuples = []  # create empty list to receive new tuples

    if list_a:  # if lists are empty, skip this and return the empty list

        added_tuples = [tuple(map(  # reassign to added_tuples
            # create a summed tuple for each tuple in the list using map
            # the map runs `sum` on each equivalent value in the tuple, for
            # each tuple in the list. Work backward to understand this:
            # `for i in range(len(list_a))` means we have an iterator value for
            # each tuple in the list. we use the iterator value to select which
            # tuple we are referencing (both the same, i.e. equivalent) within
            # the list using `list_a[i], list_b[i]`. finally, we use `zip` to
            # perform something (sum) on every item within those iterable
            # objects, i.e. sum the first item of list_a[0] with the first item
            # of list_b[0]. continue until there are no more items in list_a[0]
            # or list_b[0] (unequal lengths of tuples will ignore the extra
            # values in the longer tuple I think!). once that zip is complete,
            # it moves on to the next `i` value, so it will sum the first item
            # of list_a[1] with the first item of list_b[1]. this continues
            # until the entire list of tuples has been iterated through.
            sum, zip(list_a[i], list_b[i]))) for i in range(len(list_a))]

    return(added_tuples)  # I think you know what this does ;P

    # Oh dear, there's nothing here!

    # My crap solution

    # Your attempt is not a crap solution, it is purely your first attempt!
    # Don't beat yourself up, think about what you knew 12 months ago and
    # compare that with what you know now. Your solution also looks like it
    # should work which is a really awesome thing!

    """def add_tuple_lists(list_a, list_b):
        new_list = []
        for i in range(0, len(list_a)):
            new_tuple = []
            for n in range(0, len(list_a[i])):
                new_int = list_a[i][n] + list_b[i][n]
                new_tuple.append(new_int)
            new_list.append(tuple(new_tuple))
        return new_list"""
