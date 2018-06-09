class ZomatoLocation():
    def __init(self, entity_type, entity_id, title, latitude, longitude, city_id, city_name, country_id, country_name):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id
        self.country_name = country_name

    @classmethod
    def get_locations(kls):
        pass
