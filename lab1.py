import requests
print("The version of requests library is: " + requests.__version__ + "\n")

print("Here is the Google homepage: ")
r = requests.get("http://www.google.com")
print(r)
print(r.text + "\n")

print("Here is the source code of my python script: ")
code = requests.get("https://raw.githubusercontent.com/PeterSunJY/CMPUT404-Lab1/master/lab1.py")
code = code.text
print(code)