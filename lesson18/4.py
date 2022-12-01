class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def view(self):
        print(f"Я - User и могу просматривать содержимое! ")
class Moderator(User):
    def __init__(self, group_id):
        super().__init__('зачем', "почему")
        self.group_id = group_id
    def view(self):
        print(f"Я - moderator и я могу просматривать содержимое!")
    def redact(self):
         print(f"Я - moderator и я могу редактировать содержимое!")

user_1 = User('Зачем', 'мой пин код от сбера 0420')
user_2 = Moderator("чего")
user_1.view()
user_2.redact()
user_2.view()