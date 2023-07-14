import requests

api_key = "313c2f226816d4b2aec26a9af48b3f59574a0"

link = input('Enter a Link :') # the URL you want to shorten
name = input('Give your Link a name :') # preferred name in the URL

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={link}&name={name}"

# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)