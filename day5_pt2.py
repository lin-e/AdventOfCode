import hashlib
current_index = 0;
output_key = "________"
while True:
    new_hash = hashlib.md5(("wtnhxymk" + str(current_index)).encode('utf-8')).hexdigest()
    #print(new_hash, "[", output_key, "]", str(current_index)) 
    if new_hash.startswith("00000"):
        if new_hash[5] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            index = int(new_hash[5])
            if output_key[index] == "_":
                temp_list = list(output_key)
                temp_list[index] = new_hash[6]
                output_key = "".join(temp_list)
                print(output_key)
    current_index += 1
    if not "_" in list(output_key):
        break
print(output_key)
