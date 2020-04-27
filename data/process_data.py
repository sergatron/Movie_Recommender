
"""
MovieTweeting Data: https://github.com/sidooms/MovieTweetings/tree/master/recsyschallenge2014
Publication: http://crowdrec2013.noahlab.com.hk/papers/crowdrec2013_Dooms.pdf

"""

import numpy as np
import pandas as pd
from datetime import datetime

# Read in the datasets
print("Getting data...")
movies = pd.read_csv('https://raw.githubusercontent.com/sidooms/MovieTweetings/master/latest/movies.dat',
                     delimiter='::',
                     header=None,
                     names=['movie_id', 'movie', 'genre'],
                     dtype={'movie_id': object},
                     engine='python',
                     encoding='utf-8')
reviews = pd.read_csv('https://raw.githubusercontent.com/sidooms/MovieTweetings/master/latest/ratings.dat',
                      delimiter='::',
                      header=None,
                      names=['user_id', 'movie_id', 'rating', 'timestamp'],
                      dtype={'movie_id': object, 'user_id': object, 'timestamp': object},
                      engine='python',
                      encoding='utf-8')


# =============================================================================
# Extract Movie Title and Year
# =============================================================================
print('Cleaning movies data...')
# extract movie names, strip whitespaces
movies['movie_name'] = movies['movie'].str.split('(', expand=True)[0].str.strip()

# extract movie year
movies['year'] = movies['movie'].str.split('(', expand=True)[1].str.strip(")")

# drop original 'movie' column
movies.drop('movie', axis=1, inplace=True)

# check length of 'year', should not be longer than 4 digits
assert (movies['year'].apply(len) > 4).sum() < 1


# =============================================================================
# Dummy Variables for Centuries
# =============================================================================
# convert dtype to integer
movies['year'] = movies['year'].astype(np.uint16)

# extract movie century
movies_1900 = (movies['year'] >= 1900) & (movies['year'] < 2000)
movies['2000'] = np.where(movies['year'] > 2000, 1, 0)
movies['1900'] = np.where(movies_1900, 1, 0)
movies['1800'] = np.where(movies['year'] < 1900, 1, 0)

# check years; each row should not sum to more than 1
assert ~any(movies[['2000', '1900', '1800']].sum(axis=1) > 1)


# =============================================================================
# Genres
# =============================================================================

# split genres, append to list
genre_cat = []
for item in movies['genre'].str.split('|'):
    try:
        genre_cat.extend(item)
    except:
        pass
# pull out unique set of genres from list
categories = list(set(genre_cat))


#### Build DataFrame with Categories as Dummy Variables

# DataFrame with all categories seperated
category_df = pd.DataFrame(columns=categories, index=movies.index)
movies = pd.concat([movies, category_df], axis=1)

# convert dtype to string; avoids errors due to NaNs being floats
movies['genre'] = movies['genre'].astype(str)

# iterate over category; check if genre contains category
for item in categories:
    movies[item] = np.where(movies['genre'].str.contains(item), 1, 0)



# =============================================================================
# Reviews Data Processing
# =============================================================================
print('Cleaning reviews data...')
reviews['timestamp'] = reviews['timestamp'].astype(np.int32)

# extract date and time using 'apply'
reviews['date'] = reviews['timestamp'].apply(lambda X: str(datetime.fromtimestamp(X)))
reviews['year'] = reviews['timestamp'].apply(lambda X: datetime.fromtimestamp(X).year)
reviews['month'] = reviews['timestamp'].apply(lambda X: datetime.fromtimestamp(X).month)

reviews['day_of_week'] = reviews['timestamp'].apply(lambda X: datetime.fromtimestamp(X).weekday())
reviews['day'] = reviews['timestamp'].apply(lambda X: datetime.fromtimestamp(X).day)



# =============================================================================
# Write to File
# =============================================================================
print("Writing clean data to file...")
movies.to_csv("data/movies_clean.csv")
reviews.to_csv("data/reviews_clean.csv")
print("Finished!")


