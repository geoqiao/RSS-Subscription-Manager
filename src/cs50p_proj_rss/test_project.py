from project import add_sub, remove_sub, help_center
import pytest


def main():
    test_add()
    # test_remove()
    test_help()


def test_help():
    assert help_center() == print("Add rss feed: python project.py add <feed link>", "\n", "Remove rss feed: python project.py remove <feed link>",
                                  "\n", "List all added feeds: python project list", "\n", "List articles: python project.py articles <feed link>")


def test_add():
    with pytest.raises(SystemExit):
        add_sub("123")


def test_remove():
    with pytest.raises(SystemExit):
        remove_sub("123")
