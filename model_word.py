# libraries
import pandas as pd
import numpy as np
import json
import seaborn as sns
import collections
import random
import itertools
import gensim.downloader as api     # for word models, not yet
from gensim.models import KeyedVectors

# import dictionaries from word.dictionaries.py
from word_dictionaries import planets, houses, sun_signs_dict # etc.

# import user data
sample = pd.read_csv('10_user_sample.csv')

# Loop through the columns ending in _sign
for col in sample.columns:
    # Check if the column name ends with '_sign'
    if col.endswith('_sign'):
        # Use apply to replace the cell values
        sample[col] = sample[col].apply(lambda x: sun_signs_dict[x])

# Loop through the columns ending in _house
for col in sample.columns:
    # Check if the column name ends with '_house'
    if col.endswith('_house'):
        # Use apply to replace the cell values
        sample[col] = sample[col].apply(lambda x: houses[x])

# Loop through others too
# next steps(?)

# Now we want to 'analize' all these words and make planet connections
# e.g. mercury_sign, mercury_house and mercury(on its own) ---> big word cluster

# Define the planets to analyze
planets = ["mercury", "venus", "mars", "sun", "moon", "jupiter", "saturn", "uranus", "neptune", "pluto"]

# Initialize a list to store the most common words for each planet
common_words = []

# Analize planet corelations
for planet in planets:
    # Combine the planet_sign and planet_house columns and count the occurrences of each word
    words = list(itertools.chain(sample[f"{planet}_sign"], sample[f"{planet}_house"]))
    word_counts = {tuple(word): words.count(word) for word in words}

    # Sort the words by their frequency and get the most common word
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    common_words = sorted_words[0][0]

# Count the occurrences of each common word across all planets
common_word_counts = collections.Counter(common_words)

# Get the top three most common words across all planets
top_three_common_words = common_word_counts.most_common(3)

# Print the top three most common words across all planets
for i, (word, count) in enumerate(top_three_common_words):
    print(f"{i + 1}. {word} ({count} occurrences)")
