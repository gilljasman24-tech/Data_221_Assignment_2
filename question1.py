import string

# Read the contents of the text file
file = open("sample-file.txt", "r", encoding="utf-8")
text = file.read()
file.close()

# Split the text into individual words
words = text.split()

cleaned_words = []

# Clean and filter each word
for word in words:
    word = word.lower()
    word = word.strip(string.punctuation)

    letter_count = 0
    for char in word:
        if char.isalpha():
            letter_count += 1

    if letter_count >= 2:
        cleaned_words.append(word)

# Count the frequency of each word
word_counts = {}

for word in cleaned_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort words by frequency in descending order
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the ten most frequent words
count = 0
for word, freq in sorted_words:
    if count == 10:
        break
    print(word + " -> " + str(freq))
    count += 1
