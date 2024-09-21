import instaloader
import os

os.system('clear')

L = instaloader.Instaloader()
print("""
  ___ ____          _                _                    
 |_ _/ ___|  _     / \   _ __   __ _| |_   _ _______ _ __ 
  | | |  _  (_)   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
  | | |_| |  _   / ___ \| | | | (_| | | |_| |/ /  __/ |   
 |___\____| (_) /_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                       |___/              

                                   """)                       
print("[•] The processing time is approximately 1 or 2 minutes.")
print("")
print("[•] Too many consecutive attempts may trigger Instagram API limits.")
print("")
username = input("[•] Instagram Username: ")
print("")
password = input("[•] Instagram Password: ")


L.login(username, password)


profile = instaloader.Profile.from_username(L.context, username)
following = set(profile.get_followees())


followers = set(profile.get_followers())


not_following_back = following - followers


print("\n[•] Users Who Do Not Follow You:")
print("-" * 30)

for idx, user in enumerate(not_following_back, start=1):
    print(f"{idx}. {user.username}")

print("-" * 30)
print(f"Total: {len(not_following_back)} user.")
