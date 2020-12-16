
# data structure
storage = [None] * 23

def djb2_hash(key):
    # get the bytes of the key
    key_bytes = key.encode()
    # start from an arbitrary prime number (larger = better) 5381
    hash_value = 5381

    # bit shift and sum up the value for each char
    for byte in key_bytes:
        hash_value = ((hash_value << 5) + hash_value) + byte
        hash_value = 5381 << 5 + 5381 + "e"
        hash_value &= 0xfffffffff # keep the number to be only 32bit


    # return the hash value
    return hash_value


def basic_hash(string):
    # take in some string
    # turn the string in to bytes
    str_bytes = string.encode()

    # set up a counter or a sum variable
    sum = 0
    # iterate over each byte
    for byte in str_bytes:
        # increment our counter / sum by the value at that byte
        sum += byte

    # pass on the value to the caller (return the sum)
    return sum % len(storage)

def hash_index(key):
    return djb2_hash(key) % len(storage)

def put(key, value):
    storage[hash_index(key)] = value

def get(key):
    return storage[hash_index(key)]


print(storage)
put("Dave", 20)
print(storage)
daves_age = get("Dave")
print(daves_age)