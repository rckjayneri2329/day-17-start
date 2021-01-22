class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1


user_1 = User(user_id="2329", username="rocky")
user_2 = User(user_id="7383", username="nerry")

print(f"{user_1.username} Followers: {user_1.followers}")
print(f"{user_1.username} Following: {user_1.following}")
print(f"{user_2.username} Followers: {user_2.followers}")
print(f"{user_2.username} Following: {user_2.following}")

user_1.follow(user_2)

print("\nAfter follow\n")
print(f"{user_1.username} Followers: {user_1.followers}")
print(f"{user_1.username} Following: {user_1.following}")
print(f"{user_2.username} Followers: {user_2.followers}")
print(f"{user_2.username} Following: {user_2.following}")