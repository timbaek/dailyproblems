
class SkipIterator:
  
  def __init__(self, lst):
    self.lst = lst
    self.skip_queue = []
    self.position = 0

  def hasNext(self):
    return self.position < len(self.lst)

  def next(self):
    if self.skip_queue != []:
      skip_num = self.skip_queue.pop(0)
      if skip_num == self.lst[self.position]:
        self.position += 1
      else:
        self.skip_queue.append(skip_num)
    
    next_num = self.lst[self.position]
    self.position += 1
    return next_num

  def skip(self, val):
    self.skip_queue.append(val)

# Tests
itr = SkipIterator([2, 3, 5, 6, 5, 7, 5, -1, 5, 10])
assert(True == itr.hasNext())
assert(2 == itr.next())
itr.skip(5)
assert(3 == itr.next())
assert(6 == itr.next())
assert(5 == itr.next())
itr.skip(5)
itr.skip(5)
assert(7 == itr.next())
assert(-1 == itr.next())
assert(10 == itr.next())
assert(False == itr.hasNext())
# itr.next(); // error
