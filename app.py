import requests

r = requests.get("https://www.youtube.com")

def get_response():
    return r.status_code
