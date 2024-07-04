# 클래스 사용 예제

import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name            # 회원 이름
        self.username = username    # 회원 아이디
        self.password = self.encrypt_password(password)

    # 비밀번호 암호화
    def encrypt_password(self, password):
        hash_obj = hashlib.sha256()         # SHA-256 해시 객체 생성
        hash_obj.update(password.encode())  # 데이터 업데이트
        hash_value = hash_obj.hexdigest(    )#해시 값 추출
        return hash_value
    
    # 회원 정보 print
    def display(self):
        print(f"회원 이름 : {self.name}, 회원 아이디: {self.username}")
    

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author        # 작성자 Member.username


# 함수 정의
def add_members(member_list, member_data):
    for name, username, password in member_data:
        member_list.append(Member(name, username, password))


def add_posts(post_list, post_data):
    for title, content, author in post_data:
        post_list.append(Post(title, content, author))


def display_member_names(member_list):
    print("")
    for member in member_list:
        print(f"회원 이름: {member.name}")
    print("")

def create_member_from_input():
    name = input("Enter member name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return Member(name, username, password)


def create_post_from_input():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    author = input("Enter post author: ")
    return Post(title, content, author)



if __name__ == "__main__":
    # 데이터 준비
    member_data = [
        ("김우린", "kimwoolina", "password1"),
        ("이상현", "sanghyun", "password2"),
        ("이새예", "saeye", "password3")
    ]

    post_data = [
        ("Title 1", "post 1 content by Lina Kim", "kimwoolina"),
        ("Title 2", "post 2 content by Lina Kim", "kimwoolina"),
        ("Title 3", "post 3 content by Lina Kim", "kimwoolina"),
        ("Title 4", "post 4 content by Sanghyun Lee", "sanghyun"),
        ("Title 5", "post 5 content by Sanghyun Lee", "sanghyun"),
        ("Title 6", "post 6 content by Sanghyun Lee", "sanghyun"),
        ("Title 7", "post 7 content by Saeye Lee", "saeye"),
        ("Title 8", "post 8 content by Saeye Lee", "saeye"),
        ("Title 9", "post 9 content by Saeye Lee", "saeye")
    ]

    # Members 리스트 생성 및 회원 인스턴스 추가
    members = []
    add_members(members, member_data)

    # Posts 리스트 생성 및 게시글 인스턴스 추가
    posts = []
    add_posts(posts, post_data)

    # 사용자 입력을 통한 회원 생성
    while True:
        members.append(create_member_from_input())
        another = input("Add another member? (yes/no): ")
        if another.lower() != 'yes':
            break

    # 회원 정보 출력
    display_member_names(members)

    # 사용자 입력을 통한 글 생성
    while True:
        posts.append(create_post_from_input())
        another = input("Add another Post? (yes/no): ")
        if another.lower() != 'yes':
            break

    # 특정 유저가 작성한 게시글의 제목 프린트
    username_to_check = "kimwoolina"
    print(f"\nPosts written by {username_to_check}:")
    for post in posts:
        if post.author == username_to_check:
            print(post.title)

    # 특정 단어가 content에 포함된 게시글의 제목 프린트
    keyword_to_check = "Lee"
    print(f"\nPosts containing '{keyword_to_check}' in content:")
    for post in posts:
        if keyword_to_check in post.content:
            print(post.title)