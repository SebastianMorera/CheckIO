# Home world solutions
from operator import itemgetter  # operator is for Most wanted letter
from typing import List, Any, Iterable  # Iterable is for Ascending List


def is_even(num: int) -> bool:
    if -1000 <= num <= 1000:
        if (num % 2) == 0:
            return True
        else:
            return False
    else:
        print("Incorrect input value")
        return False

def duplicate_zeros(donuts: list) -> list:
    res = []
    for num in donuts:
        if num == 0:
            res.append(0)
            res.append(0)
        else:
            res.append(num)
    return res

def replace_last(line: list) -> list:
    if len(line) == 0:
        return line

    line.insert(0, line.pop())
    return line


def first_word(text: str) -> str:
    word = ""
    position = 0
    wordLen = len(text)
    for character in text:
        if character.isalpha() or character == "'":
            word += character
            if position >= wordLen - 1:
                break
            if not text[position + 1].isalpha():
                if text[position + 1] != "'":
                    break
            position += 1
        else:
            position += 1
            continue
    return word


def all_the_same(elements: List[Any]) -> bool:
    res = True
    count = 0
    for elm in elements:
        if elm != elements[0]:
            res = False
            break
        else:
            count += 1
    return res


def even_the_last(array: list) -> int:
    res = 0
    if 0 <= len(array) <= 20 and all(isinstance(x, int) for x in array) and all(-100 < x < 100 for x in array):
        if len(array) != 0:
            count = 0
            for elements in array:
                if count % 2 == 0:
                    res += elements
                count += 1
            res = res * array[-1]
    else:
        print("You did not respect the precondition")

    return res


def left_join(phrases: tuple) -> str:
    res = ",".join(map(str, phrases))
    if res.find("right") != -1:
        res = res.replace("right", "left")

    return res


def backward_string_by_word(text: str) -> str:
    words = text.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence


def non_empty_lines(text: str) -> int:
    res = 0
    lines = text.split("\n")
    for line in lines:
        empty = line.isspace()
        if len(line) == 0 or empty:
            continue
        else:
            res += 1
    return res


def is_ascending(items: Iterable[int]) -> bool:
    res = False
    if len(items) == 0 or len(items) == 1:
        res = True
    else:
        i = 0
        for val in items:
            if i + 1 < len(items):
                if val < items[i + 1]:
                    res = True
                else:
                    res = False
                    break
            else:
                break
            i += 1

    return res


def remove_min_max(data: set[int], total: int) -> set[int]:
    if total != 0:
        for x in range(total):
            if len(data) >= 2:
                data.remove(min(data))
                data.remove(max(data))
            else:
                data.clear()
    return data


def sum_by_types(items: list) -> tuple[str, int]:
    res_str = ""
    res_int = 0
    for element in items:
        if isinstance(element, str):
            res_str += element
        elif isinstance(element, int):
            res_int += element
    return res_str, res_int


def sum_numbers(text: str) -> int:
    res = 0
    words = text.split()
    for element in words:
        if element.isdigit():
            res += int(element)
    return res


def absolute_sorting(values: list) -> list:
    res = []
    for val in values:
        res.append(abs(val))
    res.sort()
    for val in res:
        if val not in values:
            i = res.index(val)
            res[i] = -val
    return res


def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin)
    finish = text.find(end)
    if start != -1 and finish != -1:
        if finish <= start:
            return ""
    if start == -1:
        start = 0
        begin = ""
    if finish == -1:
        finish = len(text)
    res = text[start + len(begin):finish]
    return res


def most_wanted_letter(text: str) -> str:
    dict_letters = {}
    sentence = sorted(text.lower())
    for char in sentence:
        if char.isalpha():
            if char not in dict_letters:
                dict_letters[char] = 1
            else:
                dict_letters[char] += 1
    return max(dict_letters.items(), key=itemgetter(1))[0]


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    code += ' '
    decipher = ''
    citext = ''
    for letter in code:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1  # if i = 1 that indicates a new character
            if i == 2:  # if i = 2 that indicates a new word
                decipher += ' '  # adding space to separate words
            else:
                for char in MORSE:  # accessing the keys using their values (reverse of encryption)
                    if citext == char:
                        decipher += MORSE[char]
                        break
                citext = ''
    res = decipher.capitalize()
    return res


if __name__ == '__main__':
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Is even completed!")

    assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
    assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]
    print("Duplicate zeros completed!")

    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Replace last completed!")

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("First word completed!")

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("All the same completed!")

    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_the_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_the_last([6]) == 36, "(6)*6=36"
    assert even_the_last([]) == 0, "An empty array = 0"
    print("Even last completed!")

    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Left join completed!")

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    assert backward_string_by_word("ha ha ha   this is cool") == "ah ah ah   siht si looc"
    print("Backward each word completed!")

    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
    Lorem ipsum dolor sit amet,

    consectetur adipiscing elit
    Nam odio nisi, aliquam
                ''') == 3
    print("Non empty lines completed!")

    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Ascending list completed!")

    assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
    assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
    assert remove_min_max({8, 9, 7}, 2) == set()
    assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
    assert remove_min_max(set(), 1) == set()
    print("Shorter set completed!")

    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("Sum by type completed!")

    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
            sum_numbers(
                "This picture is an oil on canvas "
                "painting by Danish artist Anna "
                "Petersen between 1845 and 1910 year"
            )
            == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0
    print("Sum numbers completed!")

    assert absolute_sorting([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert absolute_sorting([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert absolute_sorting([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Absolute sorting completed!")

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Between markers completed!')

    assert most_wanted_letter("Hello World!") == "l", "Hello test"
    assert most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert most_wanted_letter("One") == "e", "All letter only once."
    assert most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted_letter("abe") == "a", "The First."
    assert most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("Most wanted letter completed!")

    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert (
            morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
            == "I was born in 1990"
    )
    print("Morse decoder completed!")
