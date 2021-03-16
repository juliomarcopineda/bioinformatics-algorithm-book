from exercises.chapter_1 import frequent_words, pattern_to_number


def read_rosalind_1b(path):
    text, k = None, None
    with open(path) as f:
        lines = f.readlines()
        text = lines[0]
        k = int(lines[1])
    
    return text, k


def main():
    print(pattern_to_number("GATCTTTAATTCACATTTTGGTTCTATC"))


if __name__ == "__main__":
    main()
