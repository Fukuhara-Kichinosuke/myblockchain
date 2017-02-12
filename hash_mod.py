import hashlib
m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
print(m.digest_size)
print(m.block_size)
