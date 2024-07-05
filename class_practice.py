# 클래스 사용 예제

import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name            # 회원 이름
        self.username = username    # 회원 아이디
        self.password = self.encrypt_password(password)

    # 비밀번호 암호화
    def encrypt_password(self, password):
        hash_obj = hashlib.sha256()          # SHA-256 해시 객체 생성
        hash_obj.update(password.encode())   # 데이터 업데이트
        hash_value = hash_obj.hexdigest()    # 해시 값 추출
        return hash_value
    
    # 회원 정보 print
    def display(self):
        print(f"name : {self.name} / username : {self.username}")
    

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author                # 작성자 Member.username

    # 글 정보 print
    def display(self):
        print(f"title : {self.title} / content: {self.content} / author : {self.author} ")


# 함수 정의
def add_members(member_list, member_data):
    for name, username, password in member_data:
        member_list.append(Member(name, username, password))


def add_posts(post_list, post_data):
    for title, content, author in post_data:
        post_list.append(Post(title, content, author))


def display_member_names(member_list):
    print("\n-------- New Member List --------")
    for member in member_list:
        print(f"회원 이름: {member.name}")
    print("")


def create_member_from_input():
    name = input("\nEnter member name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return Member(name, username, password)


def create_post_from_input():
    title = input("\nEnter post title: ")
    content = input("Enter post content: ")
    author = input("Enter post author: ")
    return Post(title, content, author)


# 특정유저가 작성한 게시글의 제목을 출력하는 함수
def search_post_by_username(username_to_check):
    titles = []
    for post in posts:
        if username_to_check in post.author :
            titles.append(post.title)
    if titles:
        print(f"해당 유저가 작성한 게시글 제목 리스트: {titles}")
    else:
        print("해당 유저가 작성한 게시글이 없습니다.")


# 검색어를 포함한 게시글 제목을 출력하는 함수
def search_post_by_keyword(keyword_to_check):
    titles = []
    for post in posts:
        if keyword_to_check in post.content:
            titles.append(post.title)
    if titles:
        print(f"해당 키워드가 포함된 게시글 제목 리스트: {titles}")
    else:
        print("해당 키워드로 검색된 게시글이 없습니다.")


if __name__ == "__main__":
    # 데이터 준비
    member_data = [
        ("김우린", "kimwoolina", "password1"),
        ("이상현", "sanghyun", "password2"),
        ("이새예", "saeye", "password3")
    ]

    post_data = [
        ("Title 1", "개인 프로젝트가 끝났습니다.", "kimwoolina"),
        ("Title 2", "팀 프로젝트를 시작하였습니다.", "kimwoolina"),
        ("Title 3", "깃허브를 시작하였습니다.", "kimwoolina"),
        ("Title 4", "리포지토리를 생성하였습니다.", "sanghyun"),
        ("Title 5", "브랜치를 만들고 각자 맡은 코드를 push하였습니다.", "sanghyun"),
        ("Title 6", "에러가 났습니다.", "sanghyun"),
        ("Title 7", "깃허브가 좋지만 어렵습니다. 코드리뷰를 해야합니다.", "saeye"),
        ("Title 8", "팀 프로젝트는 즐겁습니다.", "saeye"),
        ("Title 9", "코드리뷰를 하면서 많은 걸 배울 수 있었습니다.", "saeye")
    ]

    # Members 리스트 생성 및 회원 인스턴스 추가
    members = []
    add_members(members, member_data)

    # 기존 맴버 정보 출력
    print("\n-------- Member List --------")
    for member in members:
        member.display()

    # Posts 리스트 생성 및 게시글 인스턴스 추가
    posts = []
    add_posts(posts, post_data)

    # 기존 포스트 정보 출력
    print("\n--------- Post List ---------")
    for post in posts:
        post.display()

    # 사용자 입력을 통한 회원 생성
    while True:
        members.append(create_member_from_input())
        another = input("\nAdd another member? (yes/no): ")
        if another.lower() != 'yes':
            break

    # 회원 정보 출력
    display_member_names(members)

    # 사용자 입력을 통한 글 생성
    while True:
        posts.append(create_post_from_input())
        another = input("\nAdd another Post? (yes/no): ")
        if another.lower() != 'yes':
            break

username_to_check = input("\n게시글 작성자 검색: ")
search_post_by_username(username_to_check)

keyword_to_check = input("\n키워드로 게시글 검색: ")
search_post_by_keyword(keyword_to_check)