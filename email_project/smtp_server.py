from email import Email

class SMTPServer:
    
    def deliver(self, email: Email):
        print(f"[SMTP] ‘{email.subject}’ 메일을 {email.recipient}에게 수신 완료")
