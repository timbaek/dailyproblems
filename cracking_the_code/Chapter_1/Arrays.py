'''
Implementation of resizable arrays (Java) in Python
'''

class Arrays:
  def __init__(self):
    self.lst = []
    self.size = 1

  def add(self, elem):
    if self.size == len(self.lst):
      new_lst, new_size = [], self.size * 2
      for i in range(self.size):
        new_lst.append(self.lst[i])
      self.lst = new_lst
      self.size = new_size
    self.lst.append(elem)

  def remove(self, elem):
    pass

  def remove_at_ith(self, i):
    pass

  def get(self,i):
    pass