import requests

def main():
    # title, venue_name, venue_start_time, 
    url = 'http://api.eventful.com/json/events/search?&app_key=bgw8NQ28vRcNxKHB'
    params = {'keyword': 'musics', 'location': 'Minneapolis'}
    data = requests.get(url, params=params).json()
    print(data)

if __name__ == '__main__':
    main()