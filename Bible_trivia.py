prophets = {
    "Elijah": "major",
    "Elisha": "minor",
    "Jeremaiah": "major",
    "Nehemiah": "minor",
    "Ezekiel": "major",
    "Hosea": "minor",
}
disciples = {
    "Mathew": "Tax Collector",
    "Luke": "Physician",
    "John": "Fishermen",
    "Andrew": "fishermen",
    "Simon": "fishermen",
    "James": "fishermen",
}
summary = {
    "Books": 66,
    "New Testament": 27,
    "Old Testament": 39,
    "Chapters": 1189,
    "Verses": 31102,
}

bible_trivia = [prophets,disciples,summary]

for person in bible_trivia:
    if prophets:
        print("Prophets of the old Testament")
        for name, type in prophets.items():
            print(f" {name} was a {type} prophet.")

    if disciples:
        print("\nThe disciples of Christ and their occupations")
        for name, occupation in disciples.items():
            print(f"{name} was a {occupation}")

    if summary:
        print("\nHere is the summary of the bible")
        for category, number in summary.items():
            print(f"There are {number} {category}")
