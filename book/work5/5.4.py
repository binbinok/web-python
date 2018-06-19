import urllib

file = urllib.urlopen('http://helloworldbook.com/data/message.txt').read()

print(file)
