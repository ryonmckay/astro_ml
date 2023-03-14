# 0. Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import gensim.downloader as api
from gensim.models import KeyedVectors
import collections
import itertools
import random
import gzip
import shutil
## our word dictionaries
from word_dictionaries import planets, houses, sun_signs_dict #tbc


# 1. Pre-trained model

# THIS NEEDS TO BE DOWNLOADED IN SAME FOLDER - pre-trained model
url = 'https://drive.google.com/u/0/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download'

# Open .gz model in working file
with gzip.open('GoogleNews-vectors-negative300.bin.gz', 'rb') as f_in:
    with open('GoogleNews-vectors-negative300.bin', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Load pre-trained word2vec model
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)


# 2. Modeling user data

# Let's go
sample = pd.read_csv('user_ ... bla .csv') # add sample or user

# Initialize a list to store the most common words for each planet
common_words = []

# Analize planet corelations
for planet in planets:
    # Combine the planet_sign and planet_house columns and count the occurrences of each word
    words = list(itertools.chain(sample[f'{planet}_sign'], sample[f'{planet}_house']))
    word_counts = {tuple(word): words.count(word) for word in words}

    # Sort the words by their frequency and get the most common word
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    common_words.append(sorted_words[0][0])

# Flatten the list of common words and remove duplicates
flat_common_words = list(set(itertools.chain.from_iterable(common_words)))

# Count the occurrences of each common word across all planets
common_word_counts = collections.Counter()

for word in flat_common_words:
    if word in model:
        common_word_counts[word] = sum([model.similarity(word, other_word) for other_word in flat_common_words if other_word in model])

# Get the top three most common words across all planets
top_three_common_words = common_word_counts.most_common(3)

# Print the top three most common words across all planets
for i, (word, count) in enumerate(top_three_common_words):
    print(f'{i + 1}. {word}')

# Notes
# - gensim library used to load the model and to calculate word similarities.
# - we're removing duplicate words and words that are not in the model


# 3. Example output for sample person 2069

#       1. resourceful
#       2. passionate
#       3. enthusiastic

# ==> example transformation (thropugh chatGPT or?)

# Resourceful, passionate, and enthusiastic,
#   with a can-do attitude and a zest for life. 🔍💪🌟
#   You have a strong sense of purpose and direction,
#   and you approach new experiences with curiosity and energy. 🎯⚡️
