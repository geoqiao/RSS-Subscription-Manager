# RSS Subscription Manager

This repo is my CS50P final project, thanks for watching!

This is a simple Python script for managing RSS subscriptions. It can add, remove, and list RSS subscriptions, and show all articles.
 
## Usage

The RSS Subscription Manager uses the following commands:

```
python main.py <command> <url>
```

Where `command` is the command and `url` is the URL of the RSS subscription.

**Available commands:**

- `add`：Add an RSS subscription.
- `remove`：Remove an RSS subscription.
- `feeds`：Lists all subscribed RSS feeds.
- `articles`：Show  all  articles of your RSS subscriptions.

**Examples:**

```
# Add an RSS subscription
phthon main.py add https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml

# Remove an RSS subscription
phthon main.py remove https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml

# List all RSS subscriptions
phthon main.py feeds

# Show all articles of your RSS subscriptions
phthon main.py articles 
```

## Notes

- The RSS subscription URL must be a valid RSS feed link.
- When adding an RSS subscription, the subscription URL format will be checked. If the format is incorrect, an error message will be displayed.
- When removing an RSS subscription, the subscription will be deleted from the `subscriptions.csv` file.
- When listing all RSS subscriptions, the names of all subscriptions will be displayed.
- When showing all articles of your RSS subscriptions, the titles and links of all articles will be displayed.

## TODO
- [x] Support exporting to a CSV file.
- [X] Fix the bug that displays the earliest 10 articles.
- [ ] Fix typo error of this README.md.
- [ ] Remove the dependency on the `pandas` library.(For some reason, I couldn't figure out how to use the standard library `CSV`, so I introduced the dependency on the third-party library `pandas`.)

## Contributions

Contributions to the RSS Subscription Manager are welcome. You can contribute in the following ways:
- Submit bug reports or suggestions.
- Submit code changes.
- Submit issues.

## License

The RSS Subscription Manager is licensed under the MIT license