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

# Create bigrams from consecutive words
bigrams = []

for i in range(len(cleaned_words) - 1):
    bigram = cleaned_words[i] + " " + cleaned_words[i + 1]
    bigrams.append(bigram)

# Count bigram frequencies
bigram_counts = {}

for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1

# Sort bigrams by frequency in descending order
sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 5 most frequent bigrams
count = 0
for bigram, freq in sorted_bigrams:
    if count == 5:
        break
    print(bigram + " -> " + str(freq))
    count += 1
