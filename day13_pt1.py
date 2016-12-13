class point_update:
    def __init__(self, parent):
        self.end = False
        self.new = list()
        self.remove = False
class path:
    def __init__(self, parent):
        self.all = list()
        self.entity = parent
        self.start = self.entity.points[0]
        self.end = self.entity.points[1]
        self.current = self.start
        self.all.append(self.current)
    def length(self):
        used = list()
        count = 0
        for i in self.all:
            if not i in used:
                used.append(i)
                count += 1
        return count
    def copy(self, direction):
        to_return = path(self.entity)
        for single_point in self.all:
            to_return.all.append(single_point)
        to_return.all.append(self.current)
        to_return.current = self.entity.move_point(self.current, direction)
        to_return.all.append(to_return.current)
        return to_return
    def calculate(self):
        if not self.current in self.entity.used:
            self.entity.used.append(self.current)
        to_return = point_update(self)
        if self.current[0] == self.end[0] and self.current[1] == self.end[1]:
            to_return.end = True
            return to_return
        possible = list()
        for d in range(1, 5):
            next_point = self.entity.move_point(self.current, d)
            if next_point in self.all:
                continue
            if self.entity.parent.get_point(next_point[0], next_point[1]) == 0:
                continue
            if next_point in self.entity.used:
                continue
            self.entity.used.append(next_point)
            possible.append(d)
        if len(possible) == 1:
            to_return.remove = False
            next_point = self.entity.move_point(self.current, possible[0])
            self.current = next_point
            self.all.append(self.current)
            if self.current[0] == self.end[0] and self.current[1] == self.end[1]:
                to_return.end = True
        else:
            to_return.remove = True
        if len(possible) > 1:
            for d in possible:
                to_return.new.append(self.copy(d))
        return to_return
    
class entity:
    def __init__(self, parent_grid, start, end):
        self.points = [start, end]
        self.parent = parent_grid
        self.end = path(self)
        self.used = list()
        self.paths = list()
    def move_point(self, origin, direction): # function to move points, for cleaner code
        if (direction == 1): # if the direction is up
            return [origin[0], origin[1] - 1] # changes y by -1 (the top-left corner is 0,0)
        if (direction == 2): # if the direction is down
            return [origin[0], origin[1] + 1] # changes y by 1
        if (direction == 3): # if the direction is left
            return [origin[0] - 1, origin[1]] # changes x by -1
        if (direction == 4): # if the direction is right
            return [origin[0] + 1, origin[1]] # changes x by 1
        return origin # otherwise, returns the original point
    def solve(self):
        self.paths.append(path(self))
        path_found = False
        while not path_found:
            if len(self.paths) == 0:
                break
            remove = list()
            add = list()
            for single_path in self.paths:
                update = single_path.calculate()
                if update.end:
                    self.end = single_path;
                    print("Solved")
                    path_found = True
                    return True
                    break
                if update.remove:
                    remove.append(single_path)
                    if len(update.new) > 0:
                        for single in update.new:
                            add.append(single)
            for single in remove:
                self.paths.remove(single)
            for single in add:
                self.paths.append(single)
            remove[:] = []
            add[:] = []
        return path_found
class grid: # grid to hold two dimensional points
    def __init__(self, width, height): # creates new grid with specified dimensions
        self.grid_width = width # sets the width
        self.grid_height = height # sets height
        self.main_grid = list() # declares new list
        for i in range(0, self.grid_height): # for every row
            self.main_grid.append([0] * self.grid_width) # creates an array with the same size as the width
    def display(self): # displays the grid
        for y in self.main_grid: # goes through each row
            item_string = "" # makes empty string
            for x in y: # goes through each item in the row
                item_string += "#" if x == 0 else "." # appends to the string (these were designed with numbers, hence the string conversion)
            print(item_string) # displays the line
    def set_point(self, x, y, item): # sets the point on the grid
        self.main_grid[y][x] = item # ''
    def get_point(self, x, y): # gets the point from the grid
        return self.main_grid[y][x] # ''
input_number = 1364
width = 50
height = 50
main_grid = grid(width, height)
for x in range(0, width):
    for y in range(0, width):
        number = x*x + 3*x + 2*x*y + y + y*y + input_number
        binary = "{0:b}".format(number)
        if binary.count("1") % 2 == 0:
            main_grid.set_point(x, y, 1)
        else:
            main_grid.set_point(x, y, 0)
main_grid.display()
main_entity = entity(main_grid, [1, 1], [31, 39])
main_entity.solve()
print(main_entity.end.length() - 1)
