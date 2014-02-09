
# ord ('a')

# for each letter I need to read first
# and then use the chr(97) to write out the character
# chr(ord('a') + 2)



text = "map"

i=0

while i < len(text):
    print chr(ord(text[i]) + 2),
    i += 1