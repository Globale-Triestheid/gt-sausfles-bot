import mysql.connector


class DiscordDB:

    def __init__(self, client, db):
        self.db = db
        self.cursor = db.cursor()
        self.client = client

    def insert_message(self, message):
        author_id = message.author.id
        channel_id = message.channel.id
        body = message.content

        sql = "INSERT INTO messages (user_id, channel_id, body) VALUES (%s, %s, %s)"
        val = (author_id, channel_id, body)
        self.cursor.execute(sql, val)
        self.db.commit()

    def insert_user(self, user_id):
        user = self.client.fetch_user(user_id)
        username = user.name + "#" + user.discriminator

        sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
        val = (user_id, username)
        self.cursor.execute(sql, val)
        self.db.commit()

    def insert_channel(self, channel_id):
        channel = self.client.get_channel(channel_id)
        channel_name = channel.__str__()

        sql = "INSERT INTO channels (id, name) VALUES (%s, %s)"
        val = (channel_id, channel_name)
        self.cursor.execute(sql, val)
        self.db.commit()

    def check_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")

        res = self.cursor.fetchall()

        if len(res) > 0:
            return True
        else:
            return False

    def check_channel(self, channel_id):
        self.cursor.execute(f"SELECT * FROM channels WHERE id = '{channel_id}'")

        res = self.cursor.fetchall()

        if len(res) > 0:
            return True
        else:
            return False

    def update_user(self, user_id, username):
        self.cursor.execute(f"UPDATE users SET name = '{username}' WHERE id = '{user_id}'")

        self.db.commit()

    def update_channel(self, channel_id, channel_name):
        self.cursor.execute(f"UPDATE channels SET name = '{channel_name}' WHERE id = '{channel_id}'")

        self.db.commit()
