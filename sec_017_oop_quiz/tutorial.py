# Model IG users

class User:
    # pass # for future code

    # ATRIBUTES - what object has
    def __init__(self, user_id, username):
        # print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # METHODS - what object does (function attached to class)
    def follow(self, user):
        user.followers += 1
        self.following += 1
    








user_1 = User("001", "Andrej")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)