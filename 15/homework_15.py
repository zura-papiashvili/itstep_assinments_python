# 1. მომხმარებლის კლასი:
# - ინიციალიზდება მომხმარებლის სახელით, ცარიელი ლისტით პოსტებისთვის 
# და ცარიელი სეტით მეგობრებისთვის.
# - მეთოდები მოიცავს პოსტის შექმნას, პოსტის კომენტარებს, პოსტის მოწონებას.

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def add_friend(self, friend_user):
        self.friends.add(friend_user)
        friend_user.friends.add(self)

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def comment_on_post(self, post, comment_content):
        comment = Comment(comment_content, self)
        post.add_comment(comment)

    def like_post(self, post):
        post.add_like(self)
# 2. პოსტის კლასი :
# - ინიციალიზებულია შინაარსით, ავტორით, კომენტარების სიით, მოწონებების სიით
# - მეთოდები მოიცავს კომენტარის დამატებას და მოწონების დამატებას.

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = set()

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.add(user)

# 3. კომენტარების კლასი:
# - ინიციალიზებულია შინაარსით და ავტორით.

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

# 4. გამოყენება:
# - ქმნის ორ მომხმარებელს, ამეგობრებს მათ.
# - User1 ქმნის პოსტს, User2 კომენტარს აკეთებს მასზე და User1 ალაიქებს კომენტარს.
# - User1 ქმნის სხვა პოსტს და User2 ალაიქებს.

# მაგალითი
user1 = User("ლევანი")
user2 = User("ნათია")
user1.add_friend(user2)
post1 = user1.create_post("ცოდნა ძალაა - ფრენსის ბეკონი. ეს არის ერთ-ერთი ყველაზე ცნობილი გამონათქვამი, რომელიც ხაზს უსვამს განათლებისა და ინფორმაციის მნიშვნელობას ჩვენს ცხოვრებაში.")
user2.comment_on_post(post1, "ძალიან საინტერესო პოსტი, ლევან!")
user1.like_post(post1)
post2 = user1.create_post("პროგრამირება არის შენების შექმნის ხელოვნება და მეცნიერება.")
user2.like_post(post2)
print(f"{user1.username}-ის პოსტები:")
for post in user1.posts:
    print(f"- {post.content} (მოწონებები: {len(post.likes)}, კომენტარები: {len(post.comments)})")
    for comment in post.comments:
        print(f"  - კომენტარი: {comment.content} ავტორი: {comment.author.username}")

print(f"{user2.username}-ის მეგობრები: {[friend.username for friend in user2.friends]}")
print(f"{user1.username}-ის მეგობრები: {[friend.username for friend in user1.friends]}")


