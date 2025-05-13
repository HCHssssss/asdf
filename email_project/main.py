from auth_service import AuthService
from smtp_server import SMTPServer
from email_client import EmailClient

def prompt_login() -> tuple[str, str]:
    print("\n=== 로그인 === (종료하려면 빈 줄 엔터)")
    user_id = input("ID 입력: ").strip()
    if user_id == "":
        return "", ""           # 종료 신호
    user_pw = input("비밀번호 입력: ").strip()
    return user_id, user_pw

def main():
    auth = AuthService()
    smtp = SMTPServer()
    client = EmailClient(smtp, auth)

    # 1) 로그인 재시도 루프
    while True:
        uid, pw = prompt_login()
        if uid == "":           # 사용자 취소
            print("프로그램 종료")
            return
        if client.login(uid, pw):
            print("로그인 성공\n")
            break
        print("로그인 실패 – 다시 시도하세요.")

    # 2) 이메일 작성·전송
    print("\n=== 이메일 작성 ===")
    to      = input("받는 사람 이메일: ").strip()
    subject = input("제목: ").strip()
    body    = input("본문: ").strip()
    client.send_email(to, subject, body)

if __name__ == "__main__":
    main()