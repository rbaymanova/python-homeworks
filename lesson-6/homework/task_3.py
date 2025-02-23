import os
import string
from collections import Counter


def create_or_read_file():
    filename = "sample.txt"

    if not os.path.exists(filename):
        print("File not found. Let's create one.")
        text = input("Enter a paragraph: ")
        with open(filename, "w") as file:
            file.write(text)
    else:
        print("Reading existing file...")


def count_words():
    filename = "sample.txt"

    with open(filename, "r") as file:
        text = file.read().lower()  # Convert to lowercase

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()  # Split into words
    word_count = Counter(words)  # Count word frequency

    return word_count


def save_report(word_count):
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)  # Get top 5 words

    report_filename = "word_count_report.txt"
    with open(report_filename, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

    print(f"Report saved as {report_filename}")


def main():
    create_or_read_file()

    word_count = count_words()

    print(f"Total words: {sum(word_count.values())}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        print(f"{word} - {count} times")

    save_report(word_count)


if __name__ == "__main__":
    main()
