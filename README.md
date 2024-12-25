## What did I change
In this example, I just needed to start the split from `\n` instead of `:` so the purification and later the filter would be much easier without making it complex using regex.

## What would I do to make it better
To improve the script, it will be possible to add support for giving pattern instead of a string as filter to find the patterns in text files and also support for json responses.

## How the script works
1. Run `pip3 install -r requirements.txt`
2. Run `python main.py <URL>`

