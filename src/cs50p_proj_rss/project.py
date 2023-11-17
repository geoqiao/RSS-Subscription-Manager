import sys

import feedparser


def main():
    command = sys.argv[1]
    command_list = ["add", "remove", "list", "articles", "help"]
    if command not in command_list:
        sys.exit("Invalid command")
    elif command in ["add", "remove", "articles"]:
        url = sys.argv[2].strip()
        if command == "add":
            add_sub(url)
        elif command == "remove":
            remove_sub(url)
        else:
            list_all_article(url)
    elif command == "list":
        list_all_sub()
    else:
        help_center()


def add_sub(url):
    """
    这里添加RSS订阅，需要检查订阅链接格式是否符合
    """
    if feedparser.parse(url) and feedparser.parse(url).feed != {}:
        with open("subscriptions.txt", "a") as f:
            f.write(f"{feedparser.parse(url).feed.title}\t{url}\n")
            sys.exit("Successfully added!")
    else:
        sys.exit("Invalid feed url.")


def remove_sub(url):
    """
    在"subscriptions.txt"中，删除指定链接的订阅
    """
    with open("subscriptions.txt", "r") as f:
        lines = f.readlines()

    # 找到指定链接的订阅。
    for i in range(len(lines)):
        if lines[i].split("\t")[1] == url + "\n":
            lines.pop(i)
            break

    # 将修改后的RSS订阅保存到文件中。
    with open("subscriptions.txt", "w") as f:
        f.writelines(lines)

    sys.exit("Successful removal!")


def list_all_sub():
    """
    列出"subscriptions.txt"中现有的所有订阅链接
    """
    with open("subscriptions.txt", "r") as f:
        for line in f.readlines():
            print(line.split("\t")[0])


def list_all_article(url):
    """
    列出指定订阅链接/URI的所有文章
    """
    d = feedparser.parse(url)
    for n in range(0, len(d.entries)):
        if n <= 9:
            print(f"[{n+1}]", d.entries[n].title, d.entries[n].link, "\n")

    sys.stdout.write("请输入文章编号： ")
    ID = int(input())
    print(
        "Article Title: ",
        d.entries[ID - 1].title,
        "\n",
        "Article Link: ",
        d.entries[ID - 1].link,
        "\n",
        "Article Published Date",
        d.entries[ID - 1].published,
        "\n",
    )


def help_center():
    print(
        "Add rss feed: python project.py add <feed link>",
        "\n",
        "Remove rss feed: python project.py remove <feed link>",
        "\n",
        "List all added feeds: python project list",
        "\n",
        "List articles: python project.py articles <feed link>",
    )


if __name__ == "__main__":
    main()
