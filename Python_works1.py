def pow_8(num):
  if (num & (num- 1) == 0  and (num & (0x249249249249249249)) ):
    return True
  return False

print(pow_8(64)) # True

def pow_4(num):
  if (num & (num- 1) == 0  and (num & (0xAAAAAAAA >> 1)) ):
    return True
  return False

print(pow_4(256)) # True