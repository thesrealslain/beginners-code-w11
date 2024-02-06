"""
Assume for this exercise that the messaging and social media platform Discord has three types of users: 
Unverified users, a user that has verified their contact information, and a Nitro user who pays a subscription fee.
Every user has a unique ID (string) and a collection of messages that they have received. 
However, as depicted in the table below, the users have limitations on sending messages to other users based on their tiers.
Nitro users can pin messages, making them easier to locate. 
Pinned messages are displayed at the top of the user's messages when they are printed.

Type of user  /  Send Messages  /  Message Limit  /  Pinning Messages
Unverified           ❌                  ❌                 ❌
Verified             ✅           max 100 characters        ❌
Nitro                ✅              unlimited              ✅
Write a program discord.py that allows the creation of any type of user. 
You also need to test the user's ability to send, receive, view, and pin messages.
"""

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = []

    def send_message(self, content):
        self.messages.append(content)

    def view_messages(self):
        print(f"Messages for User {self.user_id}:")
        for message in self.messages:
            print(message)

    def pin_message(self, message_index):
        pass  # Pinned messages not supported for this user type - 'Unverified'


class UnverifiedUser(User):
    pass  # Unverified users cannot send, pin, or view messages


class VerifiedUser(User):
    def send_message(self, content):
        if len(content) <= 100:
            super().send_message(content)
        else:
            print("Message length exceeds the limit of 100 characters.")

    pass  # Verified users cannot pin messages


class NitroUser(User):
    def pin_message(self, message_index):
        if 0 <= message_index < len(self.messages):
            pinned_message = self.messages.pop(message_index)
            self.messages.insert(0, f"Pinned: {pinned_message}")

    pass  # Nitro users can send, pin, and view messages


def test_discord():
    user1 = UnverifiedUser("UnverifiedUser")
    user2 = VerifiedUser("VerifiedUser")
    user3 = NitroUser("NitroUser")

    user1.send_message("Hello, Unverified User!")
    user2.send_message("This is a verified user sending a message.")
    user3.send_message("Nitro users can send unlimited messages!")

    user1.view_messages()
    user2.view_messages()
    user3.view_messages()

    user2.send_message("This message is too long to be sent by a verified user" * 10)

    user3.pin_message(0)
    user3.pin_message(1)

    print("\nAfter pinning messages:")
    user3.view_messages()


if __name__ == "__main__":
    test_discord()
