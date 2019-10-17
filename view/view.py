from view.weather import getWeather

class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def show_menu(self):
        print("****Travel App****\n"
              "Enter a city and country code to see"
              " the weather, top restaurants\n andconcerts")
        print("You can find country codes at https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes ")
        city, country_code = self.getInput()
        while True:
            choice = int(input("Menu \n1:5 Day Weather Forecast \n2:Restaurants \n3:Concerts \n4:Exit\n"))
            if choice == 1:
                self.showWeather(city,country_code)
            elif choice == 2:
                self.showRestaurant
            elif choice == 3:
                self.showConcerts
            elif choice == 4:
                break
            else:
                print("Unknown option selected")





    def showWeather(self, city, country_code):
        got_data = getWeather(city, country_code)
        if got_data is False:
            self.show_menu()
    def showRestaurant(self):

        return None

    def showConcerts(self):

        return None

    def getInput(self):
        city = input("City: ")
        country_code = input("Country Code: ")
        return city, country_code
        # receiving user input



