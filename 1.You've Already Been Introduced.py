import urllib.request

request = urllib.request.Request('http://placekitten.com/')

try:
    response = urllib.request.urlopen(request)
    kittens = response.read()
    print(kittens[559:1000].decode('UTF-8'))
except urllib.request.URLError as e:
    print('No kittez. Got an error code:', e)
