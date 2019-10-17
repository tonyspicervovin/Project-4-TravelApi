

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert_restaurant(self, restaurant):
        self.db.insert_restaurant(restaurant)
