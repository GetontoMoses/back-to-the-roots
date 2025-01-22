guestlist = ["Angeline", "Virginia", "Keru"]
guestlist.insert(0, "Mufasa")
guestlist.insert(3, "Aaron")

print(guestlist)
removed_guest = [1,2,3]

for index in sorted(removed_guest, reverse=True):
    guestlist.pop(index)

print(guestlist)

print("Unfortunately the event is canceled!!!")

guestlist.clear()

print(guestlist)
