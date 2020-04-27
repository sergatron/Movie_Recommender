# Movie Recommendations (Work in Progress...)

There are numerous ways of making recommendations to users or friends. Simple recommendations can be made using most popular movies at the time of request, or by asking a few simple questions about favorite genres and/or actors. There is no wrong way to do it but there some important things to keep in mind. 

### Business Goals
We can say that there are four main criteria needed to make successful recommendations:
 - Relevance
 - Novelty
 - Serendipity
 - Diversity
 
Relevance may be the obvious one to focus on to begin with. It's a good way to engage with a potential customer and provide some initial relevant recommendations for a product, song, or movie. However, knowing basic human psychology, too much of a good thing is bad. Simply recommending similar items every single time may tire out a customer with boredom. Therefore, it's important to add something that provides additional surprise, excitement, and curiosity.

This recommender utilizes multiple methods to provide movie recommendations to users based on **Ranking**, **Content**, **Collaborative Filtering**, and **Matrix Factorization (FunkSVD)** with the aim to hit all four business goals and maximize retention of customers. 


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
