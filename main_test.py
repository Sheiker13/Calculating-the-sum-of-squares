def test_process_numbers():
    assert process_numbers([1, 2, 3, 4, 5, -2, -4]) == 20
    assert process_numbers([]) == 0
    assert process_numbers([2, -4, 4, -8]) == 20
    assert process_numbers([-1, -2, -3, -4]) == 0
    assert process_numbers([0, 1, 2, 3, 4, 5]) == 20

test_process_numbers()

if __name__ == "__main__":
    print(process_numbers([1, 2, 3, 4, 5, -2, -4]))