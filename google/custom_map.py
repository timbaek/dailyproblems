'''

Design a list with the follwoing methods:

'''

class CustomMap:
  def __init__(self):
    self.dict = {}
    self.not_set_all = {}
    self.set_all_val = -1

  def set(self, key, val):
    self.dict[key] = val
    self.not_set_all[key] = val

  def get(self, key):
    if key not in self.dict:
      return None
    elif key in self.dict and key in self.not_set_all:
      return self.dict.get(key)
    else:
      return self.set_all_val

  def setAll(self, val):
    self.not_set_all.clear()
    self.set_all_val = val


# Test 1
custom_map = CustomMap()
custom_map.set(0, 1)
assert(1 == custom_map.get(0))
custom_map.set(1, 2)
assert(2 == custom_map.get(1))
custom_map.setAll(5)
assert(5 == custom_map.get(0))
assert(5 == custom_map.get(1))
assert(None == custom_map.get(2))
custom_map.set(2, 7)
assert(5 == custom_map.get(0))
assert(5 == custom_map.get(1))
assert(7 == custom_map.get(2))
