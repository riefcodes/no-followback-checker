import json


def extract_username(item):
    data_list = item.get('string_list_data', [])
    if data_list:
        data = data_list[0]
        if 'value' in data and data['value']:
            return data['value']

    title = item.get('title')
    if title:
        return title

    if data_list:
        href = data_list[0].get('href', '')
        if href:
            return href.rstrip('/').split('/')[-1].replace('_u/', '')

    return None

# 1. Load the people you follow
with open('following.json', 'r') as file:
    following_data = json.load(file)

# Extract usernames from the following list
following = set()
for item in following_data['relationships_following']:
    username = extract_username(item)
    if username:
        following.add(username)

# 2. Load the people who follow you
with open('followers_1.json', 'r') as file:
    followers_data = json.load(file)

# Extract usernames from the followers list
followers = set()
for item in followers_data:
    username = extract_username(item)
    if username:
        followers.add(username)

# 3. Find out who doesn't follow you back
not_following_back = following - followers

# 4. Print the results
print(f"You are following {len(following)} people.")
print(f"{len(followers)} people are following you.")
print(f"\nThere are {len(not_following_back)} people who don't follow you back:\n")

for user in sorted(not_following_back):
    print(user)