import sqlite3


class UserManager:
    def __init__(self, db_path: str):
        self.db_path: str = db_path

    def create_user(self, user_id: int, name: str, email: str):
        conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
                       (user_id, name, email))
        conn.commit()
        conn.close()

    def get_user(self, user_id: int) -> dict:
        conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user: dict = cursor.fetchone()
        conn.close()
        return user

    def update_user_email(self, user_id: int, new_email: str):
        conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("UPDATE users SET email=? WHERE id=?",
                       (new_email, user_id))
        conn.commit()
        conn.close()

    def delete_user(self, user_id: int):
        conn: sqlite3.Connection = sqlite3.connect(self.db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()
