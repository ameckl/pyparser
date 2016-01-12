import re
import os


# Define language constants
NEWLINE = os.linesep
RESERVED_WORDS = ['if', 'int', 'char', 'then', 'else', 'then', 'while', 'read', 'write']
TEXT_SEPARATORS = [';', '(', ')', '{', '}', ' ', NEWLINE, ']', '[', ',']
COMPARATORS = ['=', '==', '>', '>=', '<', '<=']
ARITHMETIC_OPERATORS = ['+', '-', '/', '*']
SEPARATORS = [';', '(', ')', '{', '}', '[', ']', ',']
SPACES = [' ', NEWLINE]
CODIFICATION_MAP = {'identifier': 0,
                    'constant': 1,
                    'if': 2,
                    'int': 3,
                    'char': 4,
                    'then': 5,
                    'else': 8,
                    'while': 9,
                    'read': 10,
                    ';': 11,
                    '+': 12,
                    '-': 13,
                    '/': 14,
                    '*': 15,
                    '=': 16,
                    '==': 17,
                    '>=': 18,
                    '<=': 19,
                    '>': 20,
                    '<': 21,
                    ')': 22,
                    '(': 23,
                    ']': 24,
                    '[': 25,
                    '{': 26,
                    '}': 27,
                    ',': 28,
                    'write': 29}


def match_identifier(text):
    """
    Match indentifier.
    :param text: Search text
    :return: True/False
    """
    return re.search(r"^[a-zA-Z][a-zA-Z0-9]{0,7}$", text)


def match_int_constant(text):
    """
    Match an integer.
    :param text: Search text
    :return: True/False
    """
    return re.search(r"^[-]*[0-9][0-9]*$", text)


def match_char_constant(text):
    """
    Match a character constant.
    :param text: Search text
    :return: True/False
    """
    return re.search(r"^'.'$", text)
