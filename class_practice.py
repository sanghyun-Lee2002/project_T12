import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name            # 회원 이름
        self.username = username    # 회원 아이디
        self.password = self.encrypt_pw(password)

    # 비밀번호 암호화
    def encrypt_pw(self, password):
        hash_obj = hashlib.sha256()         # SHA-256 해시 객체 생성
        hash_obj.update(password.encode())  # 데이터 업데이트
        hash_value = hash_obj.hexdigest()   # 해시 값 추출
        return hash_value

    # 회원 정보 print
    def display(self):
        print(f"회원 이름 : {self.name}, 회원 아이디: {self.username}")

    def __repr__(self):
        return f"{self.name}님의 회원 정보"


class Post:

    def __init__(self, title, content, author):
        self.title = title      # 타이틀
        self.content = content  # 컨텐츠
        self.author = author    # 그 외

    def display(self):
        print(
            f"[Title]{self.post}\n[author]{self.post}\n[Content]{self.post}\n")

    def __repr__(self):
        return f"{self.author}님이 작성하신 {self.title}"


# Members 리스트 생성 및 회원 인스턴스 추가
members = []

m1 = Member('이상현', 'Hyeon', '123')
m2 = Member('김우린', 'Rina', '123')
m3 = Member('이새예', 'Seyae', '123')

members.append(m1)
members.append(m2)
members.append(m3)

print(members)          # [이상현님의 회원정보, 김우린님의 회원정보, 이새예님의 회원정보]

for member in members:
    print(member.name)  # 이상현 김우린 이새예

# Members 리스트를 돌면서 회원들의 이름 프린트


# Posts 리스트 생성 및 게시글 인스턴스 추가
posts = []

for member in members:
    print(member.name)

    p1 = Post('안녕하세요', '잘 부탁드립니다.', m1.name)
    p2 = Post('Hi', 'Nice to meet you', m1.name)
    p3 = Post('Hello', 'Rock', m1.name)
    posts.append(p1)
    posts.append(p2)
    posts.append(p3)

    p4 = Post('Super Shy', '슈퍼샤이아.', m2.name)
    p5 = Post('백발백중하는 명사수', '부산친구 유명가수', m2.name)
    p6 = Post('일취월장하며 성장중', '내가 대표해 이 거리를', m2.name)
    posts.append(p3)
    posts.append(p4)
    posts.append(p5)

    p7 = Post('Super Shy', '슈퍼샤이아.', m3.name)
    p8 = Post('백발백중하는 명사수', '부산친구 유명가수', m3.name)
    p9 = Post('일취월장하며 성장중', '내가 대표해 이 거리를', m3.name)
    posts.append(p7)
    posts.append(p8)
    posts.append(p9)

    print(posts)   

    # 6-1
    for post in posts:
        if post.author == '김우린':
            print(post.title)		

    # 6-2
    certain_word = input()
    for post in posts:
        if certain_word in post.content:
            print(post.title) 		

# 특정 유저가 작성한 게시글의 제목 프린트


# 특정 단어가 content에 포함된 게시글의 제목 프린트
