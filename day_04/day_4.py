import csv
from collections import Counter

with open('input.txt') as f:
    csv_reader = csv.reader(f, delimiter=' ')
    total_unvalid = 0
    total = 0

    for row in csv_reader:
        total += 1

        for word, count in Counter(row).items():
            # Check for identical words
            if count > 1:
                total_unvalid += 1
                break

            # Since we do not have identical words, we'll look for anagrams
            # Set to -1 because we will always come across ourselves
            same_words = -1
            for word_to_compare in Counter(row).keys():
                word_counter = Counter(word)
                word_counter_previous = Counter(word_to_compare)
                if word_counter == word_counter_previous:
                    same_words += 1

            if same_words > 0:
                total_unvalid += 1
                break

    print total - total_unvalid
