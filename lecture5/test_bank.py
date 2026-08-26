from bank import value

def test_hello():
    assert value("hello") == 0

def test_h_no_hello():
    assert value("hey") == 20

def test_greeting_without_h():
    assert value("bonjour") == 100

def test_different_cases():
    assert value("HoLa") == 20

def test_multiple_words():
    assert value("Hello, how are you?") == 0