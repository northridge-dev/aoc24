import copy
from utils.files import readlines

map = [list(row) for row in readlines('06.txt')]
map_copy = copy.deepcopy(map)

class Guard:
    def __init__(self, map):
        self.map = map
        self.map_last_row = len(map) - 1
        self.map_last_col = len(map[0]) - 1
        self.current_pos = self.get_starting_pos()
        self.direction = (-1, 0)
        self.visited = {}

    def get_starting_pos(self):
        for nrow, row in enumerate(map):
            for ncol, el in enumerate(row):
                if el == '^':
                    return (nrow, ncol)
                
    def turn_right(self):
        if self.direction == (-1, 0): # up
            self.direction = (0, 1) # right
            return
        if self.direction == (0, 1): #right
            self.direction = (1, 0) # down
            return
        if self.direction == (1, 0): # down
            self.direction = (0, -1) # left
            return
        if self.direction == (0, -1): #left
            self.direction = (-1, 0) # up
            return
    
    def is_inbounds(self, pos):
        row, col = pos
        if row < 0 or row > self.map_last_row or col < 0 or col > self.map_last_col:
            return False
        return True

    def look_ahead(self):
        next_pos = (self.current_pos[0] + self.direction[0], self.current_pos[1] + self.direction[1])
        if not self.is_inbounds(next_pos):
            return None, None
        return next_pos, self.map[next_pos[0]][next_pos[1]]
    
    def mark_visited(self):
        self.visited[self.current_pos] = self.visited.get(self.current_pos, 0) + 1
        return self.visited[self.current_pos]
    
    def count_unique(self):
        return len(self.visited.keys())
    
    def move(self):
        # loop if same cell visited > 4 because of turning rules
        if self.visited.get(self.current_pos, 0) > 4:
            return False, True
        
        next_pos, look_ahead = self.look_ahead()

        if look_ahead == '#':
            self.turn_right()
            return False, False        
        
        self.mark_visited()
        
        if next_pos == None:
            return True, False
        
        self.current_pos = next_pos
        return False, False
        
    def simulate(self):
        exited = False
        loop = False
        while not exited and not loop:
            exited, loop = self.move()
        return loop
    
# simulate guard on original map to get list of potential locations        
guard = Guard(map_copy)
guard.simulate()

# only need to test locations that would be visited by the guard
possible_locs = guard.visited.keys()

loop_locs = []

# try placing the obstacle at every location on guard's path
for possible_loc in possible_locs:
    row, col = possible_loc
    m_copy = copy.deepcopy(map)
    m_copy[row][col] = '#'

    g = Guard(m_copy)
    in_loop = g.simulate()

    if in_loop:
        loop_locs.append(possible_loc)

print(len(loop_locs))
