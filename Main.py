from database.Travel_DB import SQLTravelDB
from view_model import ViewModel
from view.view import View

def main():

    travel_db = SQLTravelDB()
    travel_view_model = ViewModel(travel_db)
    travel_view = View(travel_view_model)
    travel_view.show_menu()









if __name__ == '__main__':
        main()
