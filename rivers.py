major_rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Zambezi": "Zimbabwe",
    "Tana": "Kenya",
    "Mississippi": "USA ",
}

for key, value in major_rivers.items():
    print(f"River {key} flows through {value}")

print("These are the major rivers in the world:")
for river in major_rivers:
    print(river)
