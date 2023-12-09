import csv
import os
import pprint
import sys

import feedparser
import pandas as pd


class Feed:
    def __init__(self, url, tag=None) -> None:
        self.feed_parse = feedparser.parse(url)
        self.title = self.feed_parse.feed.title
        self.link = self.feed_parse.feed.link
        self.rss_feed = url
        self.tag = tag

    def articles(self):
        """list all the articles of Feed"""
        articles = []
        for entry in self.feed_parse.entries:
            article = {"title": entry.title, "link": entry.link}
            articles.append(article)
        return articles

    def __str__(self) -> str:
        return f"{self.title} -> {self.link}"

    def __repr__(self) -> str:
        return f"Feed({self.title})"


class FeedList(object):
    def __init__(self) -> None:
        self.feeds = {}

    def add_feed(self, feed: Feed):
        if feed not in self.feeds:
            self.feeds[feed] = feed.link
        return self.feeds

    def remove_feed(self, feed: Feed):
        if feed in self.feeds:
            del self.feeds[feed]

    def show_feeds_dict(self):
        feeds_dict = {}
        if self.feeds != {}:
            for feed in self.feeds:
                feeds_dict[feed] = {
                    "title": feed.title,
                    "tag": feed.tag,
                    "link": feed.link,
                    "rss_feed": feed.rss_feed,
                }
        return feeds_dict

    def __str__(self) -> str:
        return f"Feed Dict: {self.feeds}"


def write_row_to_csv(feed: Feed, csv_name="subscription.csv"):
    if not os.path.exists(csv_name):
        # create the CSV file when it doesn't exists
        with open(csv_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Tag", "Link", "RSS_Feed"])

    with open(csv_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([feed.title, feed.tag, feed.link, feed.rss_feed])


def del_row_in_csv(feed: Feed, csv_name="subscription.csv"):
    if not os.path.exists(csv_name):
        sys.exit("no such file")
    df_feed = pd.read_csv(csv_name)
    df = df_feed[df_feed["RSS_Feed"] != feed.rss_feed]
    df.to_csv(csv_name, index=False)
    # existing = []
    # with open(csv_name, "r") as csvfile:
    #     reader = csv.reader(csvfile)

    #     for row in reader:
    #         if row[3] == feed.rss_feed:
    #             list(reader).pop()


def help_center():
    print(
        "Add rss feed: python main.py add <feed link>",
        "\n",
        "Remove rss feed: python main.py remove <feed link>",
        "\n",
        "List all added feeds: python main.py feeds",
        "\n",
        "List articles: python main.py articles",
    )


def main():
    if len(sys.argv) == 1:
        help_center()
        sys.exit()
    feedList = FeedList()
    command = sys.argv[1]
    if command == "add" or command == "remove":
        url = sys.argv[2].strip()
        feed = Feed(url)
        if command == "add":
            feedList.add_feed(feed)
            write_row_to_csv(feed)
        else:
            feedList.remove_feed(feed)
            del_row_in_csv(feed)
    elif command == "feeds" or command == "articles":
        df_feeds = pd.read_csv("subscription.csv")
        for rf in df_feeds["RSS_Feed"]:
            feed = Feed(rf)
            feedList.add_feed(feed)
            if command == "articles":
                print(pprint.pformat(feed.articles()))
        if command == "feeds":
            print(pprint.pformat(feedList.show_feeds_dict()))
    else:
        help_center()


if __name__ == "__main__":
    main()
