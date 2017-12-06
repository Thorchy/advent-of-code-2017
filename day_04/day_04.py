import csv
import os
from collections import Counter


def check_passphrase(passphrase, allow_anagrams=True):
        valid = True
        for word, count in Counter(passphrase).items():
            # Check for identical words
            if count > 1:
                valid = False
                break

            if not allow_anagrams:
                # Set to -1 because we will always come across ourselves
                same_words = -1
                for word_to_compare in Counter(passphrase).keys():
                    word_counter = Counter(word)
                    word_counter_previous = Counter(word_to_compare)
                    if word_counter == word_counter_previous:
                        same_words += 1

                if same_words > 0:
                    valid = False
                    break

        return valid


def main():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        csv_reader = csv.reader(f, delimiter=' ')
        passphrases = list(csv_reader)

    total_passphrases = len(passphrases)
    invalid = 0
    for row in passphrases:
        if not check_passphrase(row):
            invalid += 1

    print "Day 4, Half 1: {}".format(total_passphrases - invalid)

    invalid = 0
    for row in passphrases:
        if not check_passphrase(row, allow_anagrams=False):
            invalid += 1

    print "Day 4, Half 2: {}".format(total_passphrases - invalid)


def test_passphrase_allow_anagram_case_1():
    assert check_passphrase('aa bb cc dd ee'.split(' '))


def test_passphrase_allow_anagram_case_2():
    assert not check_passphrase('aa bb cc dd aa'.split(' '))


def test_passphrase_allow_anagram_case_3():
    assert check_passphrase('aa bb cc dd aaa'.split(' '))


def test_passphrase_disallow_anagram_case_1():
    assert check_passphrase('abcde fghij'.split(' '), allow_anagrams=False)


def test_passphrase_disallow_anagram_case_2():
    assert not check_passphrase('abcde xyz ecdab'.split(' '), allow_anagrams=False)


def test_passphrase_disallow_anagram_case_3():
    assert check_passphrase('a ab abc abd abf abj'.split(' '), allow_anagrams=False)


def test_passphrase_disallow_anagram_case_4():
    assert check_passphrase('iiii oiii ooii oooi oooo'.split(' '), allow_anagrams=False)


def test_passphrase_disallow_anagram_case_5():
    assert not check_passphrase('oiii ioii iioi iiio'.split(' '), allow_anagrams=False)


if __name__ == '__main__':
    main()
