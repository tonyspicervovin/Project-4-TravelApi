import requests

def main():
    # https://github.com/psf/requests/issues/3803
    # https://github.com/Yelp/yelp-fusion/issues/59
    # https://www.yelp.com/developers/documentation/v3/authentication
    
    # name, is_closed (True or False), url, rating, price, location, title 
    headers = {'Authorization' : 'Bearer ucb20Uq6G4KNJ7EHnndz-S6qwsx9g4aK3vfqGyKFn_b1j83D9-woDvbViMA1s47wt9yc4pDf7tG1KL_7UuFHZuo0Tiz3PJ1Ds39aI2236PZ6amiUxE_FaHXtkJ2WXXYx'}
    params = {'location': 'San Bruno',
          'term': 'Japanese Restaurant',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }
    url = 'https://api.yelp.com/v3/businesses/search'
    data = requests.get(url, params=params, headers=headers).json()
    
    print(data)

if __name__ == '__main__':
    main()