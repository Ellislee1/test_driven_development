from unittest.mock import patch, MagicMock

import sys
import os

# Add the src directory to the Python path
# flake8: noqa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from src.userManager import UserManager


@patch("src.userManager.sqlite3.connect")
def test_create_user(mock_connect):
    mock_cursor = MagicMock()
    mock_connect.return_value.cursor.return_value = mock_cursor

    user_manager = UserManager(db_path="dummy.db")

    user_manager.create_user(user_id=1, name="Marcel", email="marcel@example.com")

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)", (1, "Marcel", "marcel@example.com")
    )

    mock_connect.return_value.commit.assert_called_once()
    mock_connect.return_value.close.assert_called_once()


@patch("src.userManager.sqlite3.connect")
def test_get_user(mock_connect):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, "Alice", "alice@example.com")
    mock_connect.return_value.cursor.return_value = mock_cursor

    user_manager = UserManager(db_path="dummy.db")

    user = user_manager.get_user(user_id=1)

    assert user == (1, "Alice", "alice@example.com")

    mock_cursor.execute.assert_called_once_with("SELECT * FROM users WHERE id=?", (1,))

    mock_connect.return_value.close.assert_called_once()
