import git
import os
from urllib import parse
import requests
import json
import re
from datetime import datetime, timedelta
import pickle

class Editor():
    def __init__(self, root):
        self.root = root
        self.exec_path = "./.github/workflows"
        self.source_list = ['프로그래머스', '백준']


    def get_data(self, path):
        root = self.root
        exec_path = self.exec_path


        path = path.replace(f"{root}/","")
        source, level, title = path.split("/")

        repo = git.Repo(root)
        commit = next(repo.iter_commits(paths=path, max_count=1))
        create_time = commit.committed_date
        num =  title.split('.')[0].strip()
        title = title.split('.')[1].strip()
        title_info = f"[{title}](https://github.com/g0eun/Algorithm/tree/main/{parse.quote(path)})"

        if source == "프로그래머스":
            # 레벨 (1, ..., 5)
            # 출력 예시 : '${\textsf{\color{green}Lv. 2}}$'
            level_color = {"0":"blue", "1":"skyblue", "2":"green", "3":"yellow", "4":"red", "5":"blueviolet"}
            level_info = '${' +'\\textsf{\color{' + level_color[level] + "}Lv. " + level + "}}$"


            # 정답률
            url = f"https://school.programmers.co.kr/api/v2/school/challenges/?perPage=20&order=recent&search={parse.quote(title)}"
            response = json.loads(requests.get(url).text)
            acceptance_rate = f"{response['result'][0]['acceptanceRate']}%"

        elif source == "백준":
            # 레벨 (B1, B2, ..., R5)
            with open(f"{path}/README.md", "r", encoding="UTF-8") as fd:
                title_detail = fd.readline()
            level_detail =re.findall('\[([^]]+)', title_detail)[0].split(' ')
            if level_detail[1]=="IV":
                level_num = 4
            elif level_detail[1] == "V":
                level_num = 5
            else:
                level_num = level_detail[1].count("I")
            level = f"{level[0]}{level_num}"
            level_info = f"![{level}]({exec_path}/resources/img/{level}.svg)"

            # 정답률
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50", }
            response = requests.get(f"https://www.acmicpc.net/problem/{num}", headers=headers).text
            response_data = response[response.find('<tbody>'):response.find('</tbody>')]
            acceptance_rate = response_data[response_data.rfind('<td>'):response_data.rfind('</td>')][len('<td>'):]
            try:
                acceptance_rate = f"{round(float(acceptance_rate.split('%')[0]))}%"
            except:
                # 오류 확인용
                print(response)
                pass

        return [create_time, title_info, level_info, acceptance_rate]

    def make_context(self):

        root = self.root
        source_list = self.source_list

        content_data = {}

        for source in source_list:
            if source in os.listdir(root):
                content = "\n## 📚 {}\n".format(source)
                content += "| 날짜 | 제목 | 난이도 | 정답률 |\n"
                content += "| :-----: | ----- | :-----: | :-----: |\n"

                # 문제 정보 수집
                data = []
                for level in os.listdir(f"{root}/{source}"):
                    for title in os.listdir(f"{root}/{source}/{level}"):
                        data.append(self.get_data(f"{root}/{source}/{level}/{title}"))

                # 시간순 정렬
                data.sort(key=lambda x: x[0])

                # 시간 형식 변경
                for d in data:
                    d[0] = (datetime.utcfromtimestamp(d[0]) + timedelta(hours=9)).strftime("'%Y-%m-%d")

                # 마크다운 데이터 타입 생성
                data = [f"|{'|'.join(d)}|\n" for d in data]

                content += ''.join(data)

                content_data.update({source: content})

        with open(f"{root}/readmeData.pickle", "wb") as f:
            pickle.dump(content_data, f)

        return content_data

    def update_context(self):

        root = self.root

        with open(f"{root}/readmeData.pickle", "rb") as f:
            content_data = pickle.load(f)

        # Commit 이력
        repo = git.Repo(root)
        commits_list = list(repo.iter_commits())

        # 최신 변경 파일
        changed_files = []

        for x in commits_list[0].diff(commits_list[0].parents[0]):
            if x.a_blob.path not in changed_files:
                changed_files.append(x.a_blob.path)

            if x.b_blob is not None and x.b_blob.path not in changed_files:
                changed_files.append(x.b_blob.path)

        # 문제 풀이 경로 정상 업로드 확인(README.md, *.py)
        if [file.split(".")[-1] for file in changed_files] == ['md', 'py']:

            # 신규 경로 추출
            upd_source = changed_files[0].split("/")[0]
            upd_level = changed_files[0].split("/")[1]
            upd_problem = changed_files[0].split("/")[2]

            # 문제 정보 수집
            upd_data = self.get_data(f"{root}/{upd_source}/{upd_level}/{upd_problem}")
            upd_data[0] = (datetime.utcfromtimestamp(upd_data[0]) + timedelta(hours=9)).strftime("'%Y-%m-%d")

            # 문제 풀이 내역 중복 확인
            upd_content = f"|{'|'.join(upd_data)}|\n"
            if upd_content not in content_data[upd_source]:
                content_data[upd_source] += upd_content

                with open(f"{root}/readmeData.pickle", "wb") as f:
                    pickle.dump(content_data, f)

        return content_data


def main():

    root = '/home/runner/work/Algorithm/Algorithm'

    # 편집기 생성
    editor = Editor(root)


    # 내용 생성/추가

    if 'README.md' not in os.listdir(root):
        content_data = editor.make_context()

    else:
        content_data = editor.update_context()


    # README.md 작성
    context = """#
# Algorithm Practice

- 알고리즘 풀이 내역 업데이트
- 정답 제출 시, GitHub Actions를 통해 자동 배포
- 관련 사항은 워크플로우를 통해 관리  [.github/workflows](https://github.com/g0eun/Algorithm/tree/main/.github/workflows)



"""

    for source in content_data.keys():
        context += content_data[source]


    # 배포 정보 추가
    context += f"""
##
Latest Release : {(datetime.utcnow()+ timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')}"""


    # 작성 파일 저장
    with open(f"{root}/README.md", "w", encoding="UTF-8") as fd:
        fd.write(context)


if __name__ == '__main__':

    main()