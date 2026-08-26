from twttr import shorten

def test_empty_string():
    assert shorten("") == ""

def test_different_cases():
    assert shorten("BanaNa") == "BnN"

def test_only_vowles():
    assert shorten("aeiOU") == ""

def test_no_vowels():
    assert shorten("xyz") == "xyz"

def test_numbers_and_punctuation():
    assert shorten("911, what is your emergency?") == "911, wht s yr mrgncy?"