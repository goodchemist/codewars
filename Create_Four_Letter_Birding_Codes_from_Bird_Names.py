# In the world of birding there are four-letter codes for the common names of birds.
# These codes are created by some simple rules:

# If the bird's name has only one word, the code takes the first four letters of that word.
# If the name is made up of two words, the code takes the first two letters of each word.
# If the name is made up of three words, the code is created by taking the first letter from
# the first two words and the first two letters from the third word.
# If the name is four words long, the code uses the first letter from all the words.
# (There are other ways that codes are created, but this Kata will only use the four rules listed above)

# Complete the function that takes an array of strings of common bird names from North America,
# and create the codes for those names based on the rules above. The function should return an array
# of the codes in the same order in which the input names were presented.

# Additional considerations:
# The four-letter codes in the returned array should be in UPPER CASE.
# If a common name has a hyphen/dash, it should be considered a space.

# Example
# If the input array is: ["Black-Capped Chickadee", "Common Tern"]
# The return array would be: ["BCCH", "COTE"]

def bird_code(arr):
    name_arr = []
    for word_string in arr:

        word_string = word_string.replace('-', ' ')
        word_list = word_string.split(' ')

        if len(word_list) == 1:
            name_arr.append(word_list[0][:4].upper())
        elif len(word_list) == 2:
            name_arr.append(word_list[0][:2].upper() + word_list[1][:2].upper())
        elif len(word_list) == 3:
            name_arr.append(word_list[0][0].upper() + word_list[1][0].upper() + word_list[2][:2].upper())
        else:
            name = ''
            for item in word_list:
                name += item[0]
            name_arr.append(name.upper())

    return name_arr


assert bird_code(["American Redstart", "Northern Cardinal", "Pine Grosbeak", "Barred Owl", "Starling", "Cooper's Hawk",
                  "Pigeon"]) == ["AMRE", "NOCA", "PIGR", "BAOW", "STAR", "COHA", "PIGE"]
assert bird_code(
    ["Great Crested Flycatcher", "Bobolink", "American White Pelican", "Red-Tailed Hawk", "Eastern Screech Owl",
     "Blue Jay"]) == ["GCFL", "BOBO", "AWPE", "RTHA", "ESOW", "BLJA"]
assert bird_code(["Black-Crowned Night Heron", "Northern Mockingbird", "Eastern Meadowlark", "Dark-Eyed Junco",
                  "Red-Bellied Woodpecker"]) == ["BCNH", "NOMO", "EAME", "DEJU", "RBWO"]
assert bird_code(
    ["Scarlet Tanager", "Great Blue Heron", "Eastern Phoebe", "American Black Duck", "Mallard", "Canvasback", "Merlin",
     "Ovenbird"]) == ["SCTA", "GBHE", "EAPH", "ABDU", "MALL", "CANV", "MERL", "OVEN"]
assert bird_code(
    ["Fox Sparrow", "White-Winged Crossbill", "Veery", "American Coot", "Sora", "Northern Rough-Winged Swallow",
     "Purple Martin"]) == ["FOSP", "WWCR", "VEER", "AMCO", "SORA", "NRWS", "PUMA"]
