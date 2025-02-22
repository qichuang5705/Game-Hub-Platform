import requests

url = "https://b991-123-21-18-22.ngrok-free.app/"
headers = {
    "User-Agent": "MyCustomAgent"  # Dùng một User-Agent tùy chỉnh
}

response = requests.get(url, headers=headers)
print(response.text)
