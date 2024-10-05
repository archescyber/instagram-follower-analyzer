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

# Dosya adı oluşturuluyor
filename = f"{username}-analyze.txt"

# Verileri dosyaya yazma işlemi
with open(filename, "w") as file:
    file.write("Users Who Do Not Follow You Back:\n")
    file.write("-" * 30 + "\n")
    for idx, user in enumerate(not_following_back, start=1):
        file.write(f"{idx}. {user.username}\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total: {len(not_following_back)} user.\n")

print("\n[•] Users Who Do Not Follow You:")
print("-" * 30)

for idx, user in enumerate(not_following_back, start=1):
    print(f"{idx}. {user.username}")

print("-" * 30)
print(f"Total: {len(not_following_back)} user.")
print(f"\n[•] The data has been saved in {filename}.")
