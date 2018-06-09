from .zomatouser import ZomatoUser

class ZomatoReview():
    class __init__(self, rating, review_text, review_id, rating_color, review_time_friendly, rating_text, timestamp, likes, user, comments_count):
        self.rating = rating
        self.review_text = review_text
        self.review_id = review_id
        self.rating_color = rating_color
        self.review_time_friendly = review_time_friendly
        self.rating_text = rating_text
        self.timestamp = timestamp
        self.likes = likes
        self.user = user
        self.comments_count = comments_count
        self.best_rated_restaurants = best_rated_restaurants
        self.popularity = popularity

    @classmethod
    def get_reviews(kls):
        pass
