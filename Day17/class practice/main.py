class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1


user_1 = User("01", "Liane")
print(user_1.name)
