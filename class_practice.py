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


class Post:
    pass


# Members 리스트 생성 및 회원 인스턴스 추가
members = []


# Members 리스트를 돌면서 회원들의 이름 프린트


# Posts 리스트 생성 및 게시글 인스턴스 추가
posts = []


# 특정 유저가 작성한 게시글의 제목 프린트


# 특정 단어가 content에 포함된 게시글의 제목 프린트


