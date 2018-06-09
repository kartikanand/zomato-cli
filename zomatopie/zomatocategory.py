from .zomato import ZomatoAPIRequest

class ZomatoCategory():
    """
        Zomato category class
    """

    api_end_point = 'categories'

    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<{0} : {1}>'.format(self.category_id, self.name)

    @classmethod
    def get_categories(kls):
        zomato_request = ZomatoAPIRequest()
        zomato_request.make_request(kls.api_end_point)

        resp = zomato_request.response
        try:
            categories = resp['categories']
        except KeyError:
            raise

        category_lst = []
        for category_dict in categories:
            try:
                category = category_dict['categories']
                category_id = category['id']
                category_name = category['name']
            except KeyError:
                raise

            zomato_category = ZomatoCategory(category_id, category_name)
            category_lst.append(zomato_category)

        return category_lst
