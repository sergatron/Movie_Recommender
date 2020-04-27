# Movie Recommendations

This recommender utilizes multiple methods to provide movie recommendations to users based on **Ranking**, **Content**, **Collaborative Filtering**, and **Matrix Factorization (FunkSVD)**. 

# Data
The data is obtained from [MovieTweetings](https://github.com/sidooms/MovieTweetings). Two files are downloaded, `movies`, and `reviews`. Some data processing is required to extract movie titles, year, centuries, and genres from the `movies` dataset. As for the `reviews` dataset, from the `timestamp` variable, things like date, year, month, day, and day of week are extracted to be used additional features.


# References
 - https://github.com/sidooms/MovieTweetings/tree/master/recsyschallenge2014
 - https://blog.dominodatalab.com/recommender-systems-collaborative-filtering/
 - https://www.semanticscholar.org/paper/Item-Weighting-Techniques-for-Collaborative-Baltrunas-Ricci/3e9ebcd9503ef7375c7bb334511804d1e45127e9
 - https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e
 - https://link.springer.com/referenceworkentry/10.1007%2F978-3-319-17885-1_1580
 - https://ebaytech.berlin/deep-learning-for-recommender-systems-48c786a20e1a
 - https://cxl.com/blog/survey-response-scales/
 - https://gab41.lab41.org/recommender-systems-its-not-all-about-the-accuracy-562c7dceeaff


# Acknowledgement
**Udacity's** ***Data Science Nanodegree*** - this project was part of the program
