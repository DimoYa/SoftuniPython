class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


line = input()
emails = []
while not line == "Stop":
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

sent_emails = [int(ind) for ind in input().split(", ")]

for i in sent_emails:
    emails[i].send()

for mail in emails:
    print(mail.get_info())


