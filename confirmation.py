unconfirmed_users = [
    "Mimi",
    "React",
    "Native",
    "Angualar",
    "Django",
    "JabaScript",
]

confirmed = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    
    print(f"Verifying users: {current_users.title()}")
    
    confirmed.append(current_users)
print(f"The following users have been confirmed: ")
for confirmed_users in confirmed:
    print(confirmed_users)