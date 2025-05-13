class AuthService:
    
    def __init__(self):
        # 사용자 계정 목록
        self._users = {
            "user1": "pass1",
            "user2": "pass2",
            "user3": "pass3",
            "user4": "pass4",
            "user5": "pass5",
        }

    def authenticate(self, user_id: str, password: str) -> bool:
        return self._users.get(user_id) == password
