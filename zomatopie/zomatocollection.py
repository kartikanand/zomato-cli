class ZomatoCollection():
    def __init__(self, collection_id, title, url, description, image_url, res_count, share_url):
        self.collection_id = collection_id
        self.title = title
        self.url = url
        self.description = description
        self.image_url = image_url
        self.res_count = res_count
        self.share_url = share_url

    @classmethod
    def get_collections(kls):
        pass
