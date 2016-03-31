import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
print(response.status_code)

# see more about HTTP status codes
# here: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
