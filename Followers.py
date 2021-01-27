class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
# A function inside a class is called a Method.
# def blah(): outside of a class is a function
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("sid", "siddharth")
user2 = User("kenny", "Kendall")

user2.follow(user1)
print(user2.followers)
print(user2.following)
print(user1.followers)
print(user1.following)

