ls = [1,6,11,7,2]

def middlefunc(ls:list,target:int):
  d = {}
  for i in range(len(ls)):
    res = target - ls[i]
    if res in d:
      return d[res],i
    d[ls[i]] = i

print(middlefunc(ls,8))  # (0, 3)
print(middlefunc(ls,18)) # (2, 3)