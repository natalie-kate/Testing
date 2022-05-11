import project

def test_small_tuples():
    # Let's add together two lists, each containing 4 tuples of length 2
    list_a = [(1, 1), (1, 1), (2, 2)]
    list_b = [(2, 3), (3, 2), (1, 1)]

    expected_result = [(3, 4), (4, 3), (3, 3)]

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result

def test_big_tuples():
    # Let's add together two lists, each containing 2 tuples of length 5
    list_a = [(1, 2, 3, 4, 5), (5, 6, 7, 8, 9)]
    list_b = [(5, 4, 3, 2, 1), (1, 1, 1, 1, 1)]

    expected_result = [(6, 6, 6, 6, 6), (6, 7, 8, 9, 10)]

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result

def test_empty_lists():
    # Let's just check that adding two empty lists produces an empty list
    list_a = []
    list_b = []

    expected_result = []

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result
