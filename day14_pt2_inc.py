import hashlib
salt = "abc"

def stretch(key):
    last_item = key
    for i in range(0, 2017):
        last_item = hashlib.md5((last_item).encode('utf-8')).hexdigest()
    return last_item
def is_key(index):
    global salt
    new_hash = stretch(salt + str(index))
    last_char = None
    rep_string = None
    for i in range(0, len(new_hash)):
        char = new_hash[i]
        if char == last_char:
            try:
                if char == new_hash[i + 1]:
                    rep_string = char
                    break
            except:
                return False
        last_char = char
    if rep_string == None:
        return False
    for i in range(index + 1, index + 1001):
        check_hash = stretch(salt + str(i))
        if "".join([rep_string] * 5) in check_hash:
            return True
    return False
count = 0
index = 0
while True:
    print(index)
    if is_key(index):
        count += 1
        print(count, index)
    if count == 64:
        break
    index += 1
print(index)
