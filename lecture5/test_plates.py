from plates import is_valid

def test_valid_plate():
    assert is_valid("AAA222") == True

def test_numbers_last():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_two_letters_first():
    assert is_valid("A23456") == False
    assert is_valid("33456") == False

def test_correct_length():
    assert is_valid("A") == False
    assert is_valid("AAAA33333") == False

def test_no_punctuation():
    assert is_valid("AAA.34") == False
    assert is_valid("AA 346") == False
