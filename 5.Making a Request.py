import urllib.request

# Open http://placekitten.com/ for reading on line 4!
kittens = urllib.request.urlopen('http://placekitten.com/')
response = kittens.read()
body = response[559:1000]

# Add your 'print' statement here!
print(body.decode('UTF-8'))
