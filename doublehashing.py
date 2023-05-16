def double_hashing(keys, hash_table_size, double_hash_value):
    hashtable_list = [None] * hash_table_size
    for i in range (len(keys)):
        hash_key = keys[i] % hash_table_size
        if hashtable_list[hash_key] is None:
            hashtable_list[hash_key] = keys[i]
        else:
            new_hash_key = hash_key
            while hashtable_list[new_hash_key] is not None:
                steps = double_hash_value - (keys[i] % double_hash_value)
                new_hash_key = (new_hash_key + steps) % hash_table_size
            hashtable_list[new_hash_key] = keys[i]
    return hashtable_list

values = [26, 54, 94, 17, 31, 77, 44, 51]
print(double_hashing(values, 13, 5))