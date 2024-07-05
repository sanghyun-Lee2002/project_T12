import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()  # 인코딩

class Post:
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.username = username

# 멤버 인스턴스 input
def member_from_input():
    name = str(input("Name: ")).strip()
    username = str(input("ID: ")).lower()
    password = str(input("Password: ")).strip()
    return Member(name, username, password)

# 포스트 인스턴스 input
def post_from_input():
    title = str(input("Post Title: ")).strip()
    content = str(input("Post Content: ")).strip()
    return Post(title, content, username=None)

members = []
posts = []

# 첫 번째 멤버 정보와 포스트 3개 입력
def add_members_and_posts(members, posts):
    print("\nEnter the information")
    member = member_from_input()
    members.append(member)

    print("\nPost information")
    for _ in range(3):
        post = post_from_input()
        posts.append(post)




# # 두 번째 멤버 정보와 포스트 3개 입력
# print("\n두 번째 멤버 정보")
# member2 = member_from_input()
# members.append(member2)
#
# print("\n두 번째 포스트 3개")
# for _ in range(3):
#     post = post_from_input()
#     posts.append(post)
#
# # 세 번째 멤버 정보와 포스트 3개 입력
# print("\n세 번째 멤버 정보")
# member3 = member_from_input()
# members.append(member3)
#
# print("\n세 번째 포스트 3개")
# for _ in range(3):
#     post = post_from_input()
#     posts.append(post)

# 새로운 멤버 정보 출력 함수
def member_info(members):
    print("\n Mew Member")
    for member in members:
        print(f"이름: {member.name}, ID: {member.username}")

# 새로운 멤버의 포스트 정보 툴력 함수
def post_info(posts):
    print("\n New Memnber's Post")
    for post in posts:
        post.display_post()


# members 리스트를 돌면서 회원들의 이름을 출력하는 함수
def member_name():
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



add_members_and_posts(members, posts)
keyword = input("검색할 키워드를 입력해주세요: ")
search_post(keyword)
