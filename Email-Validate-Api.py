import requests
import json

url = "https://api.zerobounce.net/v1/validate"
apikey = "7b74c5712089471ba365d9ecb799833e"
email = "ravi.ddroshan@gmail.com"

parameter = {"email": email, "apikey": apikey}

res = requests.get(url,parameter)

detail = res.json()


print(detail["status"] +" Email")
print(detail["sub_status"])
