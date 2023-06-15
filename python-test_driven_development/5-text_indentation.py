#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text: a string to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    prev = False
    for i in range(len(text)):
        if prev is True:
            prev = False
            if text[i] == ' ':
                continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()
            print()
            prev = True
