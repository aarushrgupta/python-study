unconfirmed_users = ['Alice', 'Brian', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifiying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users have benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
