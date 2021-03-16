from exercises.chapter_1 import frequent_words


def read_rosalind_1b(path):
    text, k = None, None
    with open(path) as f:
        lines = f.readlines()
        text = lines[0]
        k = int(lines[1])
    
    return text, k


def main():
    path_1b = "input_data/rosalind_ba1b.txt"
    text, k = read_rosalind_1b(path_1b)
    results = frequent_words(text, k)
    print(" ".join(results))


if __name__ == "__main__":
    main()
