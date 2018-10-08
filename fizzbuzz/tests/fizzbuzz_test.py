import fizzbuzz

def test_should_display_fizz_when_divisible_by_3():
    result = fizzbuzz.run(6)

    assert result == "fizz"



def test_should_display_buzz_when_divisible_by_5():
    result = fizzbuzz.run(20)

    assert result == "buzz"

def test_should_display_fizzbuzz_when_divisible_by_3_and_5():
    result = fizzbuzz.run(15)

    assert result == "fizzbuzz"    

def test_should_display_input_when_not_divisible_by_3_and_5():
    result = fizzbuzz.run(8)

    assert result == 8    