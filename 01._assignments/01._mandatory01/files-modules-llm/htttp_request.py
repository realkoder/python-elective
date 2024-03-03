import requests
from requests import HTTPError

response = requests.get("https://api.github.com")


# if response.status_code == 200:
#     print('Success!')    
# elif response.status_code == 404:
#     print('Not Found.')


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
# could also be done by parsing a list of tuples
#requests.get('https://api.github.com/search/repositories', params=[('q', 'requests+language:python')])

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+


# Other HTTP METHODS
# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.options('https://httpbin.org/get')