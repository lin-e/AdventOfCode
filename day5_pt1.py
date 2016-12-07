import hashlib
current_index = 0;
output_key = ""
while True:
    new_hash = hashlib.md5(("wtnhxymk" + str(current_index)).encode('utf-8')).hexdigest()
    if new_hash.startswith("00000"):
        output_key += new_hash[5]
    current_index += 1
    if len(output_key) == 8:
        break
print(output_key)
