import random
class Boat(object):
  def __init__(self, name, max_peoples, max_speed, color_num, oars):
    self.max_peoples = max_peoples
    self.max_speed = max_speed
    self.color_num = color_num
    self.oars = oars
    self.name = name
  def __str__(self):
    return str(self.__class__.__name__) + ': ' + str(self.__dict__)
#class RaftFactory(object):
#  pass
#class SubmarineFactory(object):
#  pass
class BoatFactory(object):
  def __new__(self, num):
    return Boat(
      name='beda_'+str(num),
      max_peoples=random.randint(5, 10),
      max_speed=(random.randint(5, 10)) * 10,
      color_num=random.randint(1, 5),
      oars=random.randint(1, 2)
    )
class FloatFactory(object):
  def __new__(self, num, factory):
    return factory(num)
if __name__ == '__main__':
  boats = []
  for i in range(4):
    boats.append(FloatFactory(num=i, factory=BoatFactory))
  for boat in boats:
    print(boat)