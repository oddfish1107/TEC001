import string
def word_freqency(text):
    text = text.lower()
    words = text.split()

    if not words:
        print("empty list")
        return
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    sorted_words = sorted(words_freq.items(), key=lambda item: item[1], reverse=True)
    top_5_words = sorted_words[:5]

    top5dict = {word: count for word, count in top_5_words}

    total_words = len(words)
    top_5 = sum(count for word, count in top_5_words)
    proportion = (top_5 / total_words) * 100

    print(f"Top 5 words: {top5dict}")
    print(f"Proportion of top 5 words: {total_words}")
    print(f"Proportion of top 5 words: {top_5}")

sample = """
The world is mine. The world is out there. 
The world is big, but the world is mine. 
Out of the world, it is mine. The the the out out.
"""
word_freqency("""
The world is mine. The world is out there. 
The world is big, but the world is mine. 
Out of the world, it is mine. The the the out out.
""")

