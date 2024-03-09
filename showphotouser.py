import requests

chat_id = "6612278742"
urlp = "https://t.me/shop_karel"
url = f"https://api.telegram.org/6800419925:AAHNpxtnC651xdjwqTAkeU2iD5C-Vi88uu4/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
