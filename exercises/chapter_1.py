def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    
    return count


def frequent_words(text, k):
    count_to_words = {}
    for i in range(0, len(text) - k):
        pattern = text[i: i + k]
        count = pattern_count(text, pattern)
        if count not in count_to_words:
            words = set()
            words.add(pattern)
            count_to_words[count] = words
        else:
            count_to_words[count].add(pattern)
    
    max_count = max(count_to_words.keys())

    return count_to_words[max_count]
        

symbol_to_number = {
    "A": 0,
    "C": 1,
    "G": 2,
    "T": 3
}


def pattern_to_number(pattern):
    if not pattern:
        return 0

    prefix = pattern[0: len(pattern) - 1]
    last_symbol = pattern[-1]

    number = 4 * pattern_to_number(prefix) + symbol_to_number.get(last_symbol)

    return number