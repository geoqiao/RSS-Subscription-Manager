# RSS Subscription Manager

This is a simple Python script for managing RSS subscriptions. It can add, remove, and list RSS subscriptions, and show all articles of a specified RSS subscription.
 
## Usage

The RSS Subscription Manager uses the following commands:

```
python project.py <command> <url>
```

Where `command` is the command and `url` is the URL of the RSS subscription.

**Available commands:**

- `add`：Add an RSS subscription.
- `remove`：Remove an RSS subscription.
- `list`：Lists all subscribed RSS feeds.
- `articles`：Show  the latest 10 articles of a specified RSS subscription.

**Examples:**

```
# Add an RSS subscription
phthon project.py add https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml

# Remove an RSS subscription
phthon project.py remove https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml

# List all RSS subscriptions
phthon project.py list

# Show all articles of a specified RSS subscription
phthon project.py articles https://raw.githubusercontent.com/geoqiao/gitblog/main/feed.xml
```

## Notes

- The RSS subscription URL must be a valid RSS feed link.
- When adding an RSS subscription, the subscription URL format will be checked. If the format is incorrect, an error message will be displayed.
- When removing an RSS subscription, the subscription will be deleted from the `subscriptions.txt` file.
- When listing all RSS subscriptions, the names of all subscriptions will be displayed.
- When showing all articles of a specified RSS subscription, the titles and links of all articles will be displayed. Users can enter the article number to view detailed information.

## Contributions

Contributions to the RSS Subscription Manager are welcome. You can contribute in the following ways:
- Submit bug reports or suggestions.
- Submit code changes.

## License

The RSS Subscription Manager is licensed under the MIT license