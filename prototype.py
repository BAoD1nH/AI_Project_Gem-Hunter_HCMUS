import matplotlib.pyplot as plt
from copy import deepcopy
import time

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
    # Tạo figure và axes
    fig, ax = plt.subplots()

    fig.set_size_inches(10, 10)

    # Vẽ các ô vuông
    for i in range(0, self.size):
        for j in range(0, self.size):
            if (self.map_array[i][j].value == None):
              color = "purple"
            elif (self.map_array[i][j].value == "T"):
              color = "red"
            elif (self.map_array[i][j].value == "G"):
              color = "gold"

            else:
              color = "navajowhite"
            rect = plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor="black")
            ax.add_patch(rect)
            # Ghi giá trị vào ô vuông
            ax.text(j + 0.5, i + 0.5, (self.map_array[i][j].value), ha="center", va="center", fontsize=10)

    

    # Loại bỏ các trục số
    ax.set_xticks([])
    ax.set_yticks([])

    # Cài đặt giới hạn trục
    ax.set_xlim(0, self.size)
    ax.set_ylim(self.size, 0)

    # Hiển thị ma trận
    plt.show()


#Write constraints for cells containing numbers
#To obtain a set of constraint clauses in CNF
#Generate CNFs automatically.
def generateCNF():
    pass
#Using the pysat library to find the value for each variable
# Infer the result
def solveMapPysat():
    pass
# Choose and apply an optimal algorithm to solve the CNF.
def solveMapOptimal():
    pass

#Ham phu
def printCurrentMap():
    pass



# Main
file_path = "Map/9x9/9x9.txt"
map = Map()
map.readInput(file_path)
map.printMap()
