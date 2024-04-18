import matplotlib.pyplot as plt
class Cell:
  def __init__(self, value):
    self.value = value
    self.logical_variable = 0    # True: trap, False: gem

class Map(Cell):
  def __init__(self):
    self.size = 0
    self.map_array = []
  #A logical variable is assigned to each cell of the matrix 
  #Trap = True, Gem = False, Others = Number
  def readInput(self, filename):
    with open(filename, 'r') as file:
      lines = file.readlines()
      for line in lines:
        row = line.strip().split(',')
        row_values = []
        for value in row:
          if (value.strip() == '_'):
            val = Cell(None)
            row_values.append(val)
          else:
            val = Cell(int(value.strip()))
            row_values.append(val)
        self.map_array.append(row_values)
        
      self.size = len(self.map_array)

  def printMap(self):
    for i in range(0, self.size):
      for j in range(0, self.size):
        print('N' if self.map_array[i][j].value == None else self.map_array[i][j].value, end=" ")
      print()

#Write constraints for cells containing numbers
#To obtain a set of constraint clauses in CNF
#Generate CNFs automatically.
def generateCNF():

#Using the pysat library to find the value for each variable
# Infer the result
def solveMapPysat():

# Choose and apply an optimal algorithm to solve the CNF.
def solveMapOptimal():

#Measuring running time
def bruteForce():


def backTracking():

#Ham phu
def printCurrentMap():




# Main
file_path = "Map/9x9/9x9.txt"
map = Map()
map.readFile(file_path)
map.printMap()

