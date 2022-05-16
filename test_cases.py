import project
import extra_task


def test_small_tuples():
    # Let's add together two lists, each containing 4 tuples of length 2
    list_a = [(1, 1), (1, 1), (2, 2)]
    list_b = [(2, 3), (3, 2), (1, 1)]

    expected_result = [(3, 4), (4, 3), (3, 3)]

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result

    extra = extra_task.add_tuple_lists(list_a, list_b)
    assert extra == expected_result


def test_big_tuples():
    # Let's add together two lists, each containing 2 tuples of length 5
    list_a = [(1, 2, 3, 4, 5), (5, 6, 7, 8, 9)]
    list_b = [(5, 4, 3, 2, 1), (1, 1, 1, 1, 1)]

    expected_result = [(6, 6, 6, 6, 6), (6, 7, 8, 9, 10)]

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result

    extra = extra_task.add_tuple_lists(list_a, list_b)
    assert extra == expected_result


def test_empty_lists():
    # Let's just check that adding two empty lists produces an empty list
    list_a = []
    list_b = []

    expected_result = []

    result = project.add_tuple_lists(list_a, list_b)
    assert result == expected_result

    extra = extra_task.add_tuple_lists(list_a, list_b)
    assert extra == expected_result


# extra test cases added


def test_three_lists():
    # Let's add together two lists, each containing 2 tuples of length 5
    list_a = [(1, 2, 3, 4, 5), (5, 6, 7, 8, 9)]
    list_b = [(5, 4, 3, 2, 1), (1, 1, 1, 1, 1)]
    list_c = [(1, 2, 3, 4, 5), (2, 3, 2, 3, 2)]

    expected_result = [(7, 8, 9, 10, 11), (8, 10, 10, 12, 12)]

    result = extra_task.add_tuple_lists(list_a, list_b, list_c)
    assert result == expected_result


def test_five_long_lists():
    # Let's add together two lists, each containing 2 tuples of length 5
    list_a = [
        (1, 2, 3, 4, 5),
        (5, 6, 7, 8, 9),
        (),
        (2, 3, 4),
        (0, 2),
        (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    list_b = [
        (5, 4, 3, 2, 1),
        (1, 1, 1, 1, 1),
        (),
        (5, 6, 7),
        (3, 8),
        (9, 8, 7, 6, 5, 5, 4, 3, 2)]
    list_c = [
        (1, 2, 3, 4, 5),
        (2, 3, 2, 3, 2),
        (),
        (1, 1, 1),
        (5, 5),
        (1, 1, 1, 1, 1, 1, 1, 1, 1)]
    list_d = [
        (4, 1, 4, 1, 6),
        (2, 3, 2, 3, 2),
        (),
        (1, 1, 1),
        (8, 5),
        (5, 5, 6, 7, 8, 9, 5, 12, 100)]
    list_e = [
        (1, 2, 3, 4, 5),
        (2, 3, 2, 3, 2),
        (),
        (2, 2, 2),
        (3, 9),
        (40, 50, 60, 70, 80, 90, 10, 20, 30)]

    expected_result = [
        (12, 11, 16, 15, 22),
        (12, 16, 14, 18, 16),
        (),
        (11, 13, 15),
        (19, 29),
        (56, 66, 77, 88, 99, 111, 27, 44, 142)]

    result = extra_task.add_tuple_lists(list_a, list_b, list_c, list_d, list_e)
    print(result)
    assert result == expected_result


def test_lists_with_negatives():
    # Let's add together two lists, each containing 2 tuples of length 5
    list_a = [(1, -2, 3, 4, 5), (5, 6, 7, -8, 9)]
    list_b = [(-5, 4, -3, 2, 1), (1, -1, 1, 1, 1)]
    list_c = [(1, -2, 3, 4, 5), (2, 3, -2, 3, -2)]

    expected_result = [(-3, 0, 3, 10, 11), (8, 8, 6, -4, 8)]

    result = extra_task.add_tuple_lists(list_a, list_b, list_c)
    assert result == expected_result
