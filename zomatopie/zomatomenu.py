class ZomatoMenu():
    def __init__(self, daily_menu_id, name, start_date, end_date, dishes):
        self.daily_menu_id = daily_menu_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.dishes = dishes

    @classmethod
    def get_daily_menu(kls):
        pass
