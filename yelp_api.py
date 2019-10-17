import requests

def get_restaurant_info():
    # https://github.com/psf/requests/issues/3803
    # https://github.com/Yelp/yelp-fusion/issues/59
    # https://www.yelp.com/developers/documentation/v3/authentication

    location = user_input_location()
    restaurant = user_input_restaurant_type()
    
    headers = {'Authorization' : 'Bearer ucb20Uq6G4KNJ7EHnndz-S6qwsx9g4aK3vfqGyKFn_b1j83D9-woDvbViMA1s47wt9yc4pDf7tG1KL_7UuFHZuo0Tiz3PJ1Ds39aI2236PZ6amiUxE_FaHXtkJ2WXXYx'}
    params = {'businesses' : 'name',
        'location': location,
        'term': restaurant,  
        'sort_by': 'rating'
         }
    url = 'https://api.yelp.com/v3/businesses/search'
    data = requests.get(url, params=params, headers=headers).json()

    restaurant_data = data['businesses']
    
    for info in restaurant_data:
        restaurant_name = info['name']
        location = info['location']['display_address']
        rating = info['rating']
        print(f'Name: {restaurant_name}')
        print(f'Location: {location}')
        print(f'Rating: {rating} \n')

def user_input_location():

    location_input = input('Enter the location for more information: ')
    return location_input

def user_input_restaurant_type():

    restaurant_type = input('Enter what kind of restaurant are you looking for: ')
    return restaurant_type


if __name__ == '__main__':
    main()