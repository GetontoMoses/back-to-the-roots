my_top_songs = [
    "Beba",
    "It's you",
    "Hadi Kesho",
    "Disemba",
    "Beta",
    "Aki sioni",
    "Extra Pressure",
    "Wewe",
]

# your top 3 songs of the week
print(len(my_top_songs))
print(f"Your top songs were: \n{my_top_songs[:3]}\n")

# mid level hits
moderate_hits = (len(my_top_songs) / 2) - 1
print("you moderately listened to:")
for song in  my_top_songs[int(moderate_hits):int(moderate_hits)+3]:
 print(f"\t {song}")

# last three songs
print(my_top_songs[-3:])


mwirigi_top_songs = my_top_songs[:]

my_top_songs.append("E-love")
mwirigi_top_songs.append("Tamashani")

for song in my_top_songs:
 print(song)

