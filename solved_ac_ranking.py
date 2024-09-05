import requests
import json

def get_inu_student_ranking(url, organization_id):
    response = requests.get(f"{url}?organizationId={organization_id}")
    students = json.loads(response.content.decode("utf-8")).get("items", [])
    return [student.get("handle") for student in students]

def print_ranking(handles):
    for rank, handle in enumerate(handles, start=1):
        print(f"Rank {rank} : {handle}")

# 사용할 URL과 기관 ID
url = "https://solved.ac/api/v3/ranking/in_organization"
organization_id = 355 # 355=solved.ac 인천대학교 기관 코드 

inu_student_handles = get_inu_student_ranking(url, organization_id)
print_ranking(inu_student_handles)

