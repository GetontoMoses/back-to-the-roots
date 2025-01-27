responses = {}
response_active = True

while response_active:
    name = input("What is your name: ")
    feedback = input("Which major do you take: ")
    
    responses[name] = feedback
    
    more_responses =input("Would you like someone else to respond? Answer Yes/No ")
    if more_responses == "NO" or "no":
        response_active = False
        
print("Here are the results")
for x,y in responses.items():
    print(f"{x} takes {y}")
    