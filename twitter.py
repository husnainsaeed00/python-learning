import re

url = input("whats your twitter account:").strip()
#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/", "")
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"username: {username}")
matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", "", url, re.IGNORECASE)
if matches:
    print(f"username:", matches.group(2))
