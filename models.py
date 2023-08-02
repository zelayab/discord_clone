class User:
    def _init_(self, username, password, email, birthday):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday

class Server:
    def _init_(self, name, owner_id, description):
        self.name = name
        self.owner_id = owner_id
        self.description = description

class Channel:
    def _init_(self, name, server_id, type):
        self.name = name
        self.server_id = server_id
        self.type = type

class Message:
    def _init_(self, content, user_id, channel_id):
        self.content = content
        self.user_id = user_id
        self.channel_id = channel_id