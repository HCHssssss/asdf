class Email:
    _seq = 0

    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        self.id = Email._seq; Email._seq += 1
        self.sender, self.recipient = sender, recipient
        self.subject, self.body = subject, body
