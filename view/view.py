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
        getWeather(city, country_code)

    def getInput(self):
        city = input("City: ")
        country_code = input("Country Code: ")
        return city, country_code
        # recieving user input



