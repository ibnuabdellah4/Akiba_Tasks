def count_words(text):
    words = text.split()
    return len(words)


def count_characters_excluding_spaces(text):
    count = 0
    for char in text:
        if char != " ":
            count += 1
    return count


def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count


def find_longest_word(text):
    clean_text = text.replace(".", "").replace(",", "")
    words = clean_text.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def count_word_appearances(text):
    clean_text = text.lower().replace(".", "").replace(",", "")
    words = clean_text.split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def identify_repeated_words(text):
    counts = count_word_appearances(text)
    repeated = []
    for word, count in counts.items():
        if count > 1:
            repeated.append(word)
    return repeated

sample_text = "Python is useful and Python is powerful."

vowels, consonants = count_vowels_and_consonants(sample_text)

print("Sample Text:", sample_text)
print("Word Count:", count_words(sample_text))
print("Characters (excluding spaces):", count_characters_excluding_spaces(sample_text))
print(f"Vowels: {vowels}, Consonants: {consonants}")
print("Longest Word:", find_longest_word(sample_text))
print("Word Frequencies:", count_word_appearances(sample_text))
print("Repeated Words:", identify_repeated_words(sample_text))