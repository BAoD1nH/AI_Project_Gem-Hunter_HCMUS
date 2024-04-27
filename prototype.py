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

#Measuring running time
def bruteForce(map):
    size = map.size
    
    def is_valid_configuration(configuration):
        # Check if the configuration satisfies all constraints
        for i in range(size):
            for j in range(size):
                cell = map.map_array[i][j]
                if cell.value is not None:
                    count_traps = sum(1 for ni, nj in neighbors(i, j) if configuration[ni][nj] == 'T')
                    if cell.value != count_traps:
                        return False
        return True
    
    def generate_configurations(configuration, idx):
        if idx == size * size:
            return is_valid_configuration(configuration)
        
        i, j = divmod(idx, size)
        
        if map.map_array[i][j].value is None:
            configuration[i][j] = 'T'
            if generate_configurations(configuration, idx + 1):
                return True
            configuration[i][j] = 'G'
            if generate_configurations(configuration, idx + 1):
                return True
            return False
        else:
            return generate_configurations(configuration, idx + 1)
    
    def neighbors(i, j):
        for ni in range(max(0, i-1), min(size, i+2)):
            for nj in range(max(0, j-1), min(size, j+2)):
                if ni != i or nj != j:
                    yield ni, nj
    
    initial_configuration = [[map.map_array[i][j].value for i in range(size)] for j in range(size)]
    
    # Generate configurations recursively
    result = generate_configurations(initial_configuration, 0)
    
    if result:
        for i in range(size):
            for j in range(size):
                if initial_configuration[i][j] == 'T':
                    map.map_array[i][j].value = "T"
                elif initial_configuration[i][j] == 'G':
                    map.map_array[i][j].value = "G"
                else:
                    map.map_array[i][j].value = map.map_array[i][j].value
        map.printMap()
    else:
        print("No solution found.")

def backtracking(map):
    size = map.size
    
    def is_valid_configuration(configuration):
        # Check if the configuration satisfies all constraints
        for i in range(size):
            for j in range(size):
                cell = map.map_array[i][j]
                if cell.value is not None:
                    count_traps = sum(1 for ni, nj in neighbors(i, j) if configuration[ni][nj] == 'T')
                    if cell.value != count_traps:
                        return False
        return True
    
    def generate_configurations(configuration, idx):
        if idx == size * size:
            return is_valid_configuration(configuration)
        
        i, j = divmod(idx, size)
        
        if map.map_array[i][j].value is None:
            for value in ['T', 'G']:
                configuration[i][j] = value
                if generate_configurations(configuration, idx + 1):
                    return True
            return False
        else:
            return generate_configurations(configuration, idx + 1)
    
    def neighbors(i, j):
        for ni in range(max(0, i-1), min(size, i+2)):
            for nj in range(max(0, j-1), min(size, j+2)):
                if ni != i or nj != j:
                    yield ni, nj
    
    initial_configuration = [['_' for _ in range(size)] for _ in range(size)]
    
    # Generate configurations recursively
    result = generate_configurations(initial_configuration, 0)
    
    if result:
        for i in range(size):
            for j in range(size):
                if initial_configuration[i][j] == 'T':
                    map.map_array[i][j].value = "T"
                else:
                    map.map_array[i][j].value = "G"
        map.printMap()
    else:
        print("No solution found.")

#Ham phu
def printCurrentMap():
    pass



# Main
file_path = "Map/5x5/5x5.txt"
map = Map()
map.readInput(file_path)
map.printMap()

bruteForce(map)
backtracking(map)
