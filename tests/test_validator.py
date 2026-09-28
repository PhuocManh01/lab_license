from src.validator import is_non_empty_text, is_positive_number


def test_is_positive_number():
    assert is_positive_number(3)


def test_is_positive_number_accepts_valid_numeric_input():
    assert is_positive_number(1)
    assert is_positive_number(2.5)


def test_is_positive_number_rejects_invalid_input():
    assert not is_positive_number("3")
    assert not is_positive_number(None)


def test_is_positive_number_rejects_empty_input():
    assert not is_positive_number("")
    assert not is_positive_number("   ")


def test_is_positive_number_handles_boundary_values():
    assert not is_positive_number(0)
    assert not is_positive_number(-0.1)
    assert is_positive_number(0.1)


def test_is_non_empty_text():
    assert is_non_empty_text("hello")
