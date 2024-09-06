import requests
import json

def get_user_info(user_id):
    url = "https://solved.ac/api/v3/search/user" #solved.ac api 불러오기
    querystring = {"query": user_id}
    headers = {
        "x-solvedac-language": "",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)
    items = json.loads(response.content.decode("utf-8")).get("items", [])

    if items:
        item = items[0]
        return { #딕셔너리 형태로 리턴
            "handle": item.get("handle"), #아이디
            "rank": item.get("rank"), #랭킹
            "solvedCount": item.get("solvedCount"), #해결한 문제 수
            "rating": item.get("rating") #레이팅
        }
    else:
        return None

def print_user_info(user_info):
    if user_info:
        print(f"Handle: {user_info['handle']}\n"
              f"Rank: {user_info['rank']}\n"
              f"Solved Count: {user_info['solvedCount']}\n"
              f"Rating: {user_info['rating']}")
    else:
        print("User not found.")

user_id = "roy6924" #유저 아이디
user_info = get_user_info(user_id)
print_user_info(user_info)
