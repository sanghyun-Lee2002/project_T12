import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hashed_pw(password)

    def hashed_pw(self, password):
        hash_obj = hashlib.sha256()
        hash_obj.update(password.encode())
        return hash_obj.hexdigest()


class Post:
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.username = username

    def display_post(self):
        print(f"Title: {self.title} / Content: {self.content} / Author: {self.username}")


# 멤버 인스턴스 생성
members = [
    Member("김우린", "lina", "1q2w3e4r"),
    Member("이상현", "shlee", "qqqq1111"),
    Member("이새예", "saeye", "1010qpqp")
]

# 포스트 인스턴스 생성
posts = [
    Post("개인프로젝트", "개인프로젝트 과제인 업다운 게임 코드와 가위바위보 게임 코딩이 끝났습니다.", "lina"),
    Post("팀프로젝트", "팀프로젝트를 시작했습니다. 팀플용 깃허브 리포지토리와 브랜치를 생성했습니다.", "shlee"),
    Post("깃허브", "코드리뷰를 하기 위해 깃허브 브랜치에 각자 만든 코드를 업로드 하였습니다.", "saeye")
]

# 멤버와 포스트 출력
print("Member Info")
for member in members:
    print(f"이름: {member.name}, 사용자명: {member.username}")

print("\nPost Info")
for post in posts:
    post.display_post()


# members 리스트를 돌면서 회원들의 이름 출력
for member in members:
    print(member.name)


# 검색어를 포함한 게시글 제목을 출력하는 함수
def search_post(keyword):
    titles = []
    for post in posts:
        if keyword in post.content:
            titles.append(post.title)
    if titles:
        print(f"\n해당 키워드가 포함된 게시글 제목 리스트: {titles}")
    else:
        print("\n해당 키워드로 검색된 게시글이 없습니다.")

keyword = input("검색할 키워드를 입력해주세요: ")
search_post(keyword)