'''

Design a data structure to calculate the moving product of all elements in a sliding window of size k.

'''

class SlidingWindow:

  def __init__(self, k):
    self.size = k

    self.window = []
    self.product = 1

  def add(self, val):
    if len(self.window) == self.size:
      popped = self.window.pop(0)
      
      self.product /= popped

    self.window.append(val)

    self.product *= val

  def get_product(self):
    return self.product

# Test 1
window = SlidingWindow(3)

window.add(1) # [1]
window.add(2) # [1, 2]
assert(2 == window.get_product())
window.add(3) # [1, 2, 3]
assert(6 == window.get_product())
window.add(4) # [2, 3, 4]
assert(24 == window.get_product())
