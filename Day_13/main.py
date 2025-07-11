#Display art

from art import logo, vs
from game_data import data
import random 

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

print(logo)


account_a = random.choice(data)
account_b = random.choice(data) 
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()


a_followers = account_a["follower_count"]
b_followers = account_b["follower_count"]