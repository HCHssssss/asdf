from auth_service import AuthService
from email import Email
from smtp_server import SMTPServer

class EmailClient:
    def __init__(self, server: SMTPServer, auth: AuthService):
        self.server, self.auth = server, auth
        self._login_id: str | None = None

    # 로그인 인증
    def login(self, user_id: str, password: str) -> bool:
        ok = self.auth.authenticate(user_id, password)
        self._login_id = user_id if ok else None
        return ok

    # 이메일 전송
    def send_email(self, recipient: str, subject: str, body: str):
        email = Email(self._login_id, recipient, subject, body)
        self.server.deliver(email)
        print(f"[Client] ‘{subject}’ 메일 전송 완료")
