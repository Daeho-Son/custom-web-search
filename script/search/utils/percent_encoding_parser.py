import sys
from urllib.parse import quote

initial_jamo = dict(zip(
    range(0x1100, 0x1113),
    range(0, 19))
)

vowel_jamo = dict(zip(
    range(0x1161, 0x1176),
    range(0, 21))
)

final_jamo = dict(zip(
    ['none']+list(range(0x11A8, 0x11C3)),
    range(0, 28))
)


def code_point_to_char(code_point):
    return chr(int(code_point))


def to_hangul_syllables(hangul_set):
    if len(hangul_set) == 2:
        hangul_set.append('none')
    initial = initial_jamo.get(hangul_set[0])
    vowel = vowel_jamo.get(hangul_set[1])
    final = final_jamo.get(hangul_set[2])
    return chr(initial * 588 + vowel * 28 + final + 44032)


def main():
    global initial_jamo
    global vowel_jamo
    global final_jamo
    code_points = list()
    for code_point in sys.argv[1:]:
        code_points.append(int(code_point))
    parsed_words = []
    unicode_values = []
    for i, current_word in enumerate(code_points):
        if 32 <= current_word <= 126:
            if unicode_values:
                parsed_words.append(to_hangul_syllables(unicode_values))
                unicode_values = []
            parsed_words.append(chr(current_word))
            continue
        prev_word = "" if (i - 1 < 0) else code_points[i - 1]
        next_word = "" if (i + 1 == len(code_points)) else code_points[i + 1]
        if len(unicode_values) < 2:
            unicode_values.append(current_word)
            continue
        if next_word not in vowel_jamo.keys():
            unicode_values.append(current_word)
            parsed_words.append(to_hangul_syllables(unicode_values))
            unicode_values = []
        else:
            parsed_words.append(to_hangul_syllables(unicode_values))
            unicode_values = [current_word]
    if unicode_values:
        parsed_words.append(to_hangul_syllables(unicode_values))
    return ''.join(parsed_words)


if __name__ == "__main__":
    print(main())
