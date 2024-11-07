#python -m venv env
#pip install requests
#deactivate
import requests

r = requests.get("https://www.google.com.co")
print(r)#<Response [200]>

