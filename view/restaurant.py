import requests
import os

def getRestaurant(city):
    headers = {'Authorization' : 'Bearer ucb20Uq6G4KNJ7EHnndz-S6qwsx9g4aK3vfqGyKFn_b1j83D9-woDvbViMA1s47wt9yc4pDf7tG1KL_7UuFHZuo0Tiz3PJ1Ds39aI2236PZ6amiUxE_FaHXtkJ2WXXYx'}
    params = {'location': city,
          'term': 'Restaurant',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }
    url = 'https://api.yelp.com/v3/businesses/search'
    try:
        data = requests.get(url, params=params, headers=headers).json()
        restaurant = []
        for business in data['businesses']:
            ##checks to see if the business is open
            if business['is_closed']:
                ##creates a dictionary of data from the resturaunt
                place = {'name':business['name'], 'type': business['categories'][0]['alias'], 'location':business['location']['address1'], 'rating':business['rating']}
                ##adds that restaurant to a list
                restaurant.append(place)
        ##returns a list of the restaurants
        return restaurant
    except Exception as e:
        print(f'Error Occured {e}')
