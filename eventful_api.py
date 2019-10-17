import requests

def get_event_info():
    # title, venue_name, venue_start_time,

    location = user_input_location()
    url = 'http://api.eventful.com/json/events/search?&app_key=bgw8NQ28vRcNxKHB'
    params = {'keyword': 'musics', 'location': location}
    data = requests.get(url, params=params).json()

    event_data = data['events']['event']

    for data in event_data:
        name = data['title']
        place = data['venue_name']
        address = data['venue_address']
        date = data['start_time']
        print(f'Name: {name}')
        print(f'Place: {place}')
        print(f'Address: {address}')
        print(f'Date: {date} \n')
    
def user_input_location():

    location_input = input('Enter the location for more information: ')
    return location_input
