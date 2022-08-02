# Home world solutions
from typing import List, Any


def is_even(num: int) -> bool:
    if -1000 <= num <= 1000:
        if (num % 2) == 0:
            return True
        else:
            return False
    else:
        print("Incorrect input value")
        return False


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
    print(words)
    newWords = [word[::-1] for word in words]
    print(newWords)
    newSentence = " ".join(newWords)
    print(newSentence)
    return newSentence
    # doubleSpace = text.find("  ")
    #
    # reverse = []
    # phrase = text.split(" ")
    # for word in phrase:
    #     new_word = word[::-1]
    #     reverse.append(new_word)
    #
    # if doubleSpace == -1:
    #     res = ' '.join(reverse)
    # else:
    #     reverse.insert(doubleSpace, " ")
    #     res = ' '.join(reverse)
    # return res


if __name__ == '__main__':
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Is even completed!")

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
    print("Left join completed")

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    assert backward_string_by_word("ha ha ha   this is cool") == "ah ah ah   siht si looc"
    print("Backward each word completed")
