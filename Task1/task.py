def reverse_words(input_sentence: str) -> str:
    # Rozdělení input_sentenceu na words (ignoruje vícenásobné mezery)
    words = input_sentence.strip().split()

    # Otočení pořadí
    words_reversed = words[::-1]

    # Spojení zpět do jednoho stringu
    return ' '.join(words_reversed)


sentence = "I want to work in Solutia"
result = reverse_words(sentence)
print(result)  #  Output: Solutia in work to want I


# ----------------------- Bonus #1

import re

def reverse_words_punctuation(input_sentence: str) -> str:
    parts = re.findall(r'\S+|\s+', input_sentence)

    words = [part for part in parts if not part.isspace()]
    reversed_words = list(reversed(words))

    result = []
    word_index = 0

    for part in parts:
        if part.isspace():
            result.append(part)
        else:
            result.append(reversed_words[word_index])
            word_index += 1

    return ''.join(result)

text = "I want to work in Solutia, please!"
result = reverse_words_punctuation(text)
print(result) #Output: !please, Solutia in work to want I

# ----------------------- Bonus #2
import re

def reverse_and_swap_case(input_sentence: str) -> str:
    parts = re.findall(r'\S+|\s+', input_sentence)

    words = [part for part in parts if not part.isspace()]
    reversed_words = list(reversed(words))

    result = []
    word_index = 0

    for part in parts:
        if part.isspace():
            result.append(part)
        else:
            result.append(reversed_words[word_index].swapcase())
            word_index += 1

    return ''.join(result)

# Test
text = "I want to work in Solutia, please!"
result = reverse_and_swap_case(text)
print(result)  # Output: !PLEASE, sOLUTIA IN WORK TO WANT i
