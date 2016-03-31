import urllib.request

# Add your code here!
website = urllib.request.urlopen('http://placekitten.com')
kittens = website.read()

print(kittens[559:1000].decode('UTF-8'))
