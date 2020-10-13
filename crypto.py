codeDictionary = {
    "01" : "A", "02" : "B", "03" : "C", "04" : "D", "05" : "E",
    "06" : "F", "07" : "G", "08" : "H", "09" : "I", "10" : "J",
    "11" : "K", "12" : "L", "13" : "M", "14" : "N", "15" : "O",
    "16" : "P", "17" : "Q", "18" : "R", "19" : "S", "20" : "T",
    "21" : "U", "22" : "V", "23" : "W", "24" : "X", "25" : "Y",
    "26" : "Z", "27" : ".", "28" : "!", "32" : " ",
}

rsaP = input("Please enter a prime number (p): ")
rsaQ = input("Please enter a prime number (q): ")
decrypt = input("Please enter your decryption key: ")
userString = str(input("Please enter your code: "))

# Remove any whitespace from string
userString = userString.replace(" ", "")

# If the code contains an odd number of digits, append a leading 0
if len(userString) % 2 != 0:
    userString = "0" + userString

# Create list of number pairs from user input
n = 2
map = [userString[i:i+n] for i in range(0, (len(userString) - 1), n)]

# Initializing lists
listToDecrypt = []
listDecrypted = []

# Iterate through string and convert number pairs based on decryption key
# Append to list
for i in range(0, len(map)):
    map[i] = (int(map[i]) ** int(decrypt)) % (int(rsaP) * int(rsaQ))
    listToDecrypt.append(str(map[i]))

# Iterate through list and add leading zero to single digits
for j in range(0, len(listToDecrypt)):
    if len(listToDecrypt[j]) == 1:
        listToDecrypt[j] = "0" + listToDecrypt[j]

# Iterate through list and "decrypt" values
# Append to decrypted list
for k in range(0, len(listToDecrypt)):
    l = codeDictionary.get(listToDecrypt[k])
    listDecrypted.append(l)

print("Message decrypted, please see below:")
print(''.join(listDecrypted).capitalize())
