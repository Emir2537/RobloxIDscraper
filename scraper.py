import requests
import time

initial_url = "https://friends.roblox.com/v1/users/1/followers?limit=100&sortOrder=Desc"
cursor = None

def get_followers(url):
    global cursor
    req = requests.get(url)
    req_data = req.json()
    cursor = req_data.get("nextPageCursor")
    for follower in req_data["data"]:
        yield follower["id"]
    return req_data.get("nextPageCursor")

def print_all_ids(url):
    global cursor
    page_count = 1
    while True:
        for follower_id in get_followers(url + (f"&cursor={cursor}" if cursor else "")):
            print(follower_id)
        page_count += 1
        if not cursor:
            break
        time.sleep(1)

print_all_ids(initial_url)



