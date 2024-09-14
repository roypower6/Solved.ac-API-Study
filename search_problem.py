# import requests
# import json

# def get_problem(number):
#     url = "https://solved.ac/api/v3/search/problem"
#     querystring = {"query":number,"direction":"asc","page":"1","sort":"id"}
#     headers = {
#     "x-solvedac-language": "",
#     "Accept": "application/json"
#     }
#     response = requests.get(url, headers=headers, params=querystring)
#     items=json.loads(response.content.decode("utf-8")).get("items",[])[0]
    
#     return items

# def problem_info(items):
#     problemId=items.get("problemId")
#     title=items.get("titleKo")
#     level=items.get("level")
#     avrTry=items.get("averageTries")
#     tags=items.get("tags")
#     tagslist=[]
#     for tag in tags:
#         tagslist.append(tag.get("key"))
#     return problemId, title, level, avrTry, tagslist

# def problem_info_dict(info):
#     problem_info_dict={
#         "ID":info[0],
#         "Title":info[1],
#         "level":info[2],
#         "Average Try":info[3],
#         "Tag List":info[4]
#     }
    
#     return problem_info_dict

# def print_all(dict):

#     print(f"{dict['ID']}번 문제 \"{dict['Title']}\" 입니다.\n"
#           f"사람들은 보통 이 문제를 {dict['Average Try']} 회 시도했습니다.\n"
#           f"이 문제의 난이도는 {dict['level']} level 입니다."
#     )
#     print("태그는 ",end="")
#     for i in range(len(dict["Tag List"])):
#         if i==len(dict["Tag List"])-1:
#             print(dict["Tag List"][i],end=" ")
#         else:
#             print(dict["Tag List"][i],end=", ")
#     print("입니다.")
    

# problem_id="1476"

# problem_items=get_problem(problem_id)
# info=problem_info(problem_items)
# problem_dict=problem_info_dict(info)

# print_all(problem_dict)

import requests
import json

class Problem:
    def __init__(self, problem_id):
        self.problem_id = problem_id
        self.problem_data = self.get_problem_data()
        self.info = self.extract_info()
    
    def get_problem_data(self):
        url = "https://solved.ac/api/v3/search/problem"
        querystring = {"query": self.problem_id, "direction": "asc", "page": "1", "sort": "id"}
        headers = {
            "x-solvedac-language": "",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers, params=querystring)
        items = json.loads(response.content.decode("utf-8")).get("items", [])[0]
        return items

    def extract_info(self):
        problem_id = self.problem_data.get("problemId")
        title = self.problem_data.get("titleKo")
        level = self.problem_data.get("level")
        average_tries = self.problem_data.get("averageTries")
        tags = [tag.get("key") for tag in self.problem_data.get("tags", [])]
        return {
            "ID": problem_id,
            "Title": title,
            "Level": level,
            "Average Tries": average_tries,
            "Tags": tags
        }

    def print_info(self):
        info = self.info
        print(f"{info['ID']}번 문제 \"{info['Title']}\" 입니다.\n"
              f"사람들은 보통 이 문제를 {info['Average Tries']} 회 시도했습니다.\n"
              f"이 문제의 난이도는 {info['Level']} level 입니다.")
        print("태그는 ", end="")
        for i, tag in enumerate(info['Tags']):
            if i == len(info['Tags']) - 1:
                print(tag, end=" ")
            else:
                print(tag, end=", ")
        print("입니다.")

# 사용 예시
problem_id = "1476"
problem = Problem(problem_id)
problem.print_info()

