#
# GitHub Actions를 활용한 README 배포 자동화

- 전체 알고리즘 풀이 내역 관리
- 제출 문제 정보는 [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) 를 통해 업데이트
- 문제 경로에 풀이가 추가될 경우, **Github Actions**을 통해 자동으로 `README.md` 배포




## 📌 Github Actions 유의사항

- 작업 수행을 위해, Workflow permissions 권한 필요
- Commit 이력 전체 확인을 위해 추가 옵션 설정 (기본값은 최신 1건만 포함)
```
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```


##  📌  프로젝트 구조
```
├─.github
│  └─workflows
│      ├─resources
│      │    └─img
│      │      ├─B1.svg
│      │      ├─...
│      │      └─S5.svg
│      │
│      ├─deploy-readme.yml
│      ├─update-readme.yml
│      └─main.py **
│
├─백준
├─프로그래머스
│
├─README.md
└─readmeData.pickle
```

- `deploy-readme.yml` : 프로젝트 Workflow (1)
- `update-readme.yml` : 프로젝트 Workflow (2)  
- `main.py` : 프로젝트 실행 파일
- `README.md` : 결과 파일
- `readmeData.pickle` : README 데이터 관리


## 📌 작업 내용
1️⃣ README 신규 생성
* `deploy-readme.yml` 정의
* workflows 경로 **push** 발생 시,`README.md` 생성 (최초/재작성)
* 문제 풀이 내역 전체에 대한 데이터 수집


2️⃣ README 업데이트
* `update-readme.yml` 정의
* 문제 풀이 경로 **push** 발생 시, `README` 업데이트
* 과거 이력은 `readmeData.pickle` 통해 호출하며, 신규 추가된 항목에 대해 데이터 수집