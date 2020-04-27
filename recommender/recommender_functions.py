import numpy as np
import pandas as pd


# def load_data():
#     # load moview and reviews data
#     reviews = pd.read_csv('data/reviews_clean.csv')
#     movies = pd.read_csv('data/movies_clean.csv')

#     return movies, reviews


# def dump_data(data, filepath):
#     try:
#         dump(data, filepath)
#     except Exception as e:
#         print(e)
#         print('Failed to pickle data')


def create_user_item_matrix(reviews_path="data/reviews_clean.csv"):

    reviews = pd.read_csv(reviews_path)
    train_reviews = reviews[:500_000]
    del reviews

    usr_itm = train_reviews[['user_id', 'movie_id', 'rating']].astype(np.uint32)
    user_item_df = usr_itm.groupby(['user_id','movie_id'])['rating'].max().unstack()

    return user_item_df.values


# def load_user_item(user_item_path='data/user_item_mat.pkl'):
#     return load(user_item_path)



def get_movie_names(movie_ids, movies_df):
    '''
    Params:
    -------
        movie_ids - a list of movie_ids
        movies_df - original movies dataframe

    Returns:
        movies - a list of movie names associated with the movie_ids

    '''
    # Read in the datasets
    movie_lst = list(movies_df[movies_df['movie_id'].isin(movie_ids)]['movie_name'])

    return movie_lst


def create_ranked_df(movies, reviews):
        '''
        Params:
            movies - the movies dataframe
            reviews - the reviews dataframe

        Returns:
            ranked_movies - a dataframe with movies that are sorted by highest avg rating, more reviews, then time, and must have more than 4 ratings
        '''

        # Pull the average ratings and number of ratings for each movie
        movie_ratings = reviews.groupby('movie_id')['rating']
        avg_ratings = movie_ratings.mean()
        num_ratings = movie_ratings.count()
        last_rating = pd.DataFrame(reviews.groupby('movie_id').max()['date'])
        last_rating.columns = ['last_rating']

        # Add Dates
        rating_count_df = pd.DataFrame({'avg_rating': avg_ratings, 'num_ratings': num_ratings})
        rating_count_df = rating_count_df.join(last_rating)

        # merge with the movies dataset
        movie_recs = movies.set_index('movie_id').join(rating_count_df)

        # sort by top avg rating and number of ratings
        ranked_movies = movie_recs.sort_values(['avg_rating', 'num_ratings', 'last_rating'], ascending=False)

        # for edge cases - subset the movie list to those with only 5 or more reviews
        ranked_movies = ranked_movies[ranked_movies['num_ratings'] > 4]

        return ranked_movies


def find_similar_movies(movie_id, movies_df):
    '''
    Params:
        movie_id - a movie_id
        movies_df - original movies dataframe

    Returns:
        similar_movies - an array of the most similar movies by title
    '''
    # dot product to get similar movies
    movie_content = np.array(movies_df.iloc[:,4:])
    dot_prod_movies = movie_content.dot(np.transpose(movie_content))

    # find the row of each movie id
    movie_idx = np.where(movies_df['movie_id'] == movie_id)[0][0]

    # find the most similar movie indices - to start I said they need to be the same for all content
    similar_idxs = np.where(dot_prod_movies[movie_idx] == np.max(dot_prod_movies[movie_idx]))[0]

    # pull the movie titles based on the indices
    similar_movies = np.array(movies_df.iloc[similar_idxs, ]['movie'])

    return similar_movies


def popular_recommendations(user_id, n_top, ranked_movies):
    '''
    Params::
        user_id - the user_id (str) of the individual you are making recommendations for
        n_top - an integer of the number recommendations you want back
        ranked_movies - a pandas dataframe of the already ranked movies based on avg rating, count, and time

    Returns::
        top_movies - a list of the n_top recommended movies by movie title in order best to worst
    '''

    top_movies = list(ranked_movies['movie'][:n_top])

    return top_movies
