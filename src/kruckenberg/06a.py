from utils.files import readlines

map = [list(row) for row in readlines('06.txt')]

class Guard:
    def __init__(self, map):
        self.map = map
        self.current_pos = self.get_starting_pos()
        self.direction = (-1, 0)
        self.mark_current_pos()


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
    
    def look_ahead(self):
        next_pos = (self.current_pos[0] + self.direction[0], self.current_pos[1] + self.direction[1])
        return next_pos, self.map[next_pos[0]][next_pos[1]]
    
    def mark_current_pos(self):
        self.map[self.current_pos[0]][self.current_pos[1]] = 'X'
        return
    
    def count_unique(self):
        unique = 0
        for row in self.map:
            for pos in row:
                if pos == 'X':
                    unique += 1
        return unique
    
    def move(self):
        self.mark_current_pos()

        try: 
            next_pos, look_ahead = self.look_ahead()
        except IndexError:
            print('Exiting map. Unique positions: ', self.count_unique())
            return False

        if look_ahead == '#':
            self.turn_right()
            return True
        else:
            self.current_pos = next_pos
            return True
        
    def simulate(self):
        onmap = True
        while onmap:
            onmap = guard.move()
        
        

guard = Guard(map)
guard.simulate()