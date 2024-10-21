import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users() -> list:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    return users


def test_restore_names_name(users: list[dict[str: str]]) -> None:
    restore_names(users)
    for user in users:
        name = user.get("first_name")
        assert name is not None
