# Initiation word solutions
from typing import Iterable  # Needed for Replace first
import numpy  # Needed for Nearest value
from typing import Iterable  # Needed for Remove all before


def mult_two(a, b):
    return a * b


def number_length(a: int) -> int:
    res = str(a)
    return len(res)


def first_word(text: str) -> str:
    word = text.split()[0]
    return word


def string_length(text: str) -> int:
    return len(text)


def backward_string(val: str) -> str:
    return val[::-1]


def end_zeros(num: int) -> int:
    res = 0
    number = str(num)

    for x in number[0:len(number)]:
        if x == '0':
            res += 1
        else:
            res = 0
    return res


def max_digit(number: int) -> int:
    numbers = [int(x) for x in str(number) if x.isdigit()]
    return max(numbers)


def beginning_zeros(number: str) -> int:
    res = 0

    for x in number:
        if int(x) == 0:
            res += 1
        else:
            break

    return res


def index_power(array: list, n: int) -> int:
    if n > len(array) - 1:
        return -1
    else:
        num = pow(array[n], n)
        return num


def fizzBuzz(number: int) -> str:
    res = ""

    if number % 3 == 0:
        res = "Fizz"
        if number % 5 == 0:
            res = res + " " + "Buzz"
    elif number % 5 == 0:
        res += "Buzz"
    else:
        res = str(number)

    return res


def between_markers(text: str, begin: str, end: str) -> str:
    index = text.find(begin)
    res = ''
    for element in text[index + 1::]:
        if element == end:
            break
        else:
            res += element
    return res


def replace_first(items: list) -> Iterable:
    if len(items) == 0 or len(items) == 1:
        return items
    else:
        res = items[1::1]
        res.append(items[0])
    return res


def correct_sentence(text: str) -> str:
    if not text[0].isupper():
        text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text


def best_stock(data: dict) -> str:
    best = max(data.values())
    for stock, values in data.items():
        if values == best:
            return stock


def nearest_value(values: set, one: int) -> int:
    numbers = list(values)
    array = numpy.asarray(numbers)
    if numpy.any(array < 0):
        i = (array - one).argmin()
        return array[i]
    else:
        i = (numpy.abs(array - one)).argmin()
        return array[i]


def remove_all_before(items: list, border: int) -> Iterable:
    if items.count(border) != 0:
        return items[items.index(border):]
    else:
        return items


def non_unique_elements(data: list) -> list:
    new_list = []
    for element in data:
        count = data.count(element)
        if count >= 2:
            new_list.append(element)

    return new_list


if __name__ == '__main__':
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Multiply completed!")

    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Number length!")

    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("First word (simplify) completed!")

    assert string_length("hi") == 2
    assert string_length("CheckiO") == 7
    assert string_length("") == 0
    print("String length completed!")

    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Backward string completed!")

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("End zeros completed!")

    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Max digit completed!")

    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Beginning zeros completed!")

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Index power completed!")

    assert fizzBuzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert fizzBuzz(6) == "Fizz", "6 is divisible by 3"
    assert fizzBuzz(5) == "Buzz", "5 is divisible by 5"
    assert fizzBuzz(7) == "7", "7 is not divisible by 3 or 5"
    print("Fizz buzz completed!")

    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print("Between markers completed!")

    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Replace first completed!")

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    print("Correct sentence completed!")

    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Best stock completed!")

    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Nearest value completed!")

    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Remove all before completed!")

    assert list(non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("Non unique elements completed!")
    