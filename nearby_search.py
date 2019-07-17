import json
import requests
import time

coordinator = '21.013111, 105.799972'
keyword = 'beer'
radius = 2000


def token_key():
    with open('Google_api_key.txt', 'rt') as f:
        api_key = f.readlines()
    return api_key


def fifty_nearby_search(location, keyword, radius):
    URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json' # noqa
    parameters = {
        'location': coordinator,
        'radius': radius,
        'keyword': keyword,
        'key': token_key()}
    ses = requests.Session()
    resp = ses.get(URL, params=parameters)
    Google_data = resp.json()
    result = []
    result.extend(Google_data['results'])
    time.sleep(6)
    count = 1
    if not result:
        error_mess = Google_data['error_message']
        print(error_mess)
    while 'next_page_token' in Google_data:
        count += 1
        parameters.update({'pagetoken': Google_data['next_page_token']})
        ses_next = requests.Session()
        resp_next = ses_next.get(URL, params=parameters)
        Google_data = resp_next.json()
        result.extend(Google_data['results'])
        if 'error_message' in Google_data:
            error_mess = Google_data['error_message']
            print(error_mess[:error_mess.rfind('API') + 3]
                  + ' at session {}'.format(count))
        if len(result) > 50:
            break
        time.sleep(6)
    if count == 1:
        print('After 1 session, '
              'total nearby placeshave been got ---->>> '
              '{} places'.format(len(result)))
    else:
        print('After {} sessions, '
              'total nearby places have been got ---->>> '
              '{} places'.format(count, len(result)))
    return result


def map_generation(near_by_data):
    geojson_map = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates":[float(data['geometry']['location']['lat']),float(data['geometry']['location']['lng'])]  # noqa
                },
                "properties": {
                "Address": data['vicinity'],
                "name": data['name']
                }
            } for data in near_by_data]}
    with open('map.geojson', 'wt') as f:
        json.dump(geojson_map, f, ensure_ascii=False, indent=4)


def main():
    input_data = fifty_nearby_search(coordinator, keyword, radius)
    map_generation(input_data)


if __name__ == "__main__":
    main()
