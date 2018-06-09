class ZomatoCity():
    def __init__(self, city_id, name, country_id, country_name, is_state, state_id, state_name, state_code):
        self.city_id = city_id
        self.name = name
        self.country_id = country_id
        self.country_name = country_name
        self.is_state = is_state
        self.state_id = state_id
        self.state_name = state_name
        self.state_code = state_code

    @classmethod
    def get_cities(kls):
        pass

    @classmethod(kls):
    def get_cities_by_id(kls, id_lst, count):
        city_id_lst = ','.join(id_lst)