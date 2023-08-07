class Tower(object):
  towers = [[],[],[]]
  size = 0

  def __init__(self, size):
      # Just represetn each tower as an array of numbers. One array per tower.
      # Element 0 is the base of the tower.
      self.towers = [[],[],[]]

      # Need to remember our size as a stand alon value for later stuff
      self.size = size

      # Prime the first tower with all the elements based on size of tower.
      # The init "size" is the number of discs so the bottom disc will be of 
      # the  input size (i.e. 3 for a 3 disc stack) and then each will be one
      # less
      disc = size
      while disc > 0:
          self.towers[0].append(disc)
          disc = disc - 1

  # Move the disc on tower X to Tower Y counted as 1 to 3. Yes 0 to 2 is better but this is to teach
  # a kid and we'll get to indexing from 0 later.
  def move(self, x, y):
    assert 1 <= x <= 3, "Source Tower must be between 1 and 3"
    assert 1 <= y <= 3, "Target Tower must be between 1 and 3"

    x = x-1
    y = y-1

    # Get the size of the topmost disc on each tower, or 999 if the tower is empty
    x_size = self.towers[x][len(self.towers[x])-1] if len(self.towers[x]) > 0 else 999
    y_size = self.towers[y][len(self.towers[y])-1] if len(self.towers[y]) > 0 else 999
    assert y_size > x_size, "Target tower must be bigger then source tower"

    # Pop the value off source striaght to target!
    self.towers[y].append(self.towers[x].pop())

  def print(self):
      for i in range(self.size-1,-1,-1):
          # Disc size of tower 1, 2, and 3 respecigvely is held in text A, B, C
          # Do not print directly so we can make it either a number for a disc or
          # "|" if no disc there.
          a = self.towers[0][i] if len(self.towers[0]) > i else "|"
          b = self.towers[1][i] if len(self.towers[1]) > i else "|"
          c = self.towers[2][i] if len(self.towers[2]) > i else "|"
          print ("%s %s %s" % (a, b, c))
      print("-----")
      print("")
    


def main():
    tower = Tower(9)

    tower.print()
    tower.move(1,3)
    tower.move(1,2)
    tower.print()

if __name__ == "__main__":
    main()

