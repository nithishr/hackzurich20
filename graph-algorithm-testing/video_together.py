import requests

def create_room(video_url=r"https://www.youtube.com/watch?v=3ZRE6uVMDAo"):
    request_url = r"https://w2g.tv/rooms/create.json"
    api_key = "5dsajh1uu157cc0a0bbd7frbb6zs8cgi8si7ktwxev3u3yeub8ckqq6o0jopfmq1"
    r = requests.post(request_url, data={"w2g_api_key": api_key, "share": video_url})
    if r.ok:
        room_key = r.json()["streamkey"]
        response_url = f"https://w2g.tv/rooms/{room_key}"
    else:
        response_url = "https://w2g.tv/rooms/"
    return response_url

print(create_room())
