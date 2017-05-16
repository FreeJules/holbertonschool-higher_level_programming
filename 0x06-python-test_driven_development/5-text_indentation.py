#!/usr/bin/python3
'''
This is "5-text_indentation" module

It supplies one function, text_indentation(text)

For example:
>>> text_indentation("Dynamo: Diesel? Lee.")

'''


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of those characters: ., ? and :
    Text must be a string
    There should be no space at the beginning or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    flag1 = True
    flag2 = False
    for i in text:
        if i == ' ' and flag1:
            continue
        else:
            flag1 = False
        if i == '.' or i == '?' or i == ':':
            print('{}\n'.format(i))
            flag2 = True
        else:
            if i == ' ' and flag2:
                continue
            elif i != ' ' and flag2:
                flag2 = False
            print('{}'.format(i), end='')
