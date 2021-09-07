import requests
print("The version of requests library is: " + requests.__version__)

r = requests.get("http://www.google.com")
print(r)
print(r.text)