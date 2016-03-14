def linearSearch(lst, key):
    for i in range(0, len(lst)):
        if key == lst[i]:
            return i
    return -1  ## Meaning "else", so if not there, return this. If not there, "None" is returned.

a = list(range(2,16))

key = 0

print(linearSearch(a,key))