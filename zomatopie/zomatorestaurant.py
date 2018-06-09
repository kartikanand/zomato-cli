class ZomatoRestaurant():
    def __init__(self, id, name, url, location, average_cost_for_two, price_range, currency, thumb, featured_image, photos_url, menu_url, events_url, user_rating, has_online_delivery, is_delivering_now, deeplink, cuisines, all_reviews_count, photo_count, phone_numbers, photos, all_reviews):
        self.id = id
        self.name = name
        self.url = url
        self.location = location
        self.average_cost_for_two = average_cost_for_two
        self.price_range = price_range
        self.currency = currency
        self.thumb = thumb
        self.featured_image = featured_image
        self.photos_url = photos_url
        self.menu_url = menu_url
        self.events_url = events_url
        self.user_rating = user_rating
        self.has_online_delivery = has_online_delivery
        self.is_delivering_now = is_delivering_now
        self.deeplink = deeplink
        self.cuisines = cuisines
        self.all_reviews_count = all_reviews_count
        self.photo_count = photo_count
        self.phone_numbers = phone_numbers
        self.photos = photos
        self.all_reviews = all_reviews

    @classmethod
    def get_restaurants(kls):
        pass