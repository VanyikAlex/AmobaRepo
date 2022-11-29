class Grid:
    def __init__(self, pygame):
        self.grid = [[0 for x in range(3)] for y in range(3)]

        self.grid_lines = [((0, 200), (600, 200)),  # első horizontál vonal
                           ((0, 400), (600, 400)),  # második horizintál vonal
                           ((0, 600), (600, 600)),  # harmadik horizintál vonal
                           ((200, 0), (200, 600)),  # első vertikális vonal
                           ((400, 0), (400, 600))]  # második vertikális vonal

        self.pygame = pygame

        self.letterX = pygame.image.load('Játék/proj/images/letter_x.png')
        self.letterO = pygame.image.load('Játék/proj/images/letter_o.png')

        self.switch_letter = True

        # helyek keresése  N        NW        W        SW       S       SE      E       NE
        self.search_dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

        self.game_over = False
        self.winner_letter = ""
        self.tie_game = False  # dontetlen

    def draw(self, win):
        for line in self.grid_lines:
            self.pygame.draw.line(win, (200, 200, 200), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == "X":
                    win.blit(self.letterX, (x * 200, y * 200))
                elif self.get_cell_value(x, y) == "O":
                    win.blit(self.letterO, (x * 200, y * 200))

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def mouse_click(self, x, y, letter):
        if self.get_cell_value(x, y) == 0:
            self.switch_letter = True
            self.set_cell_value(x, y, letter)
            self.check_grid(x, y, letter)
        else:
            self.switch_letter = False

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.set_cell_value(x, y, 0)

    def is_grid_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def is_within_bounds(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def check_grid(self, x, y, letter):
        count = 1
        for index, (dirx, diry) in enumerate(self.search_dirs):
            if self.is_within_bounds(x + dirx, y + diry) and self.get_cell_value(x + dirx, y + diry) == letter:
                count += 1
                xx = x + dirx
                yy = y + diry
                if self.is_within_bounds(xx + dirx, yy + diry) and self.get_cell_value(xx + dirx, yy + diry) == letter:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0
                    if index == 0:
                        new_dir = self.search_dirs[4]
                    elif index == 1:
                        new_dir = self.search_dirs[5]
                    elif index == 2:
                        new_dir = self.search_dirs[6]
                    elif index == 3:
                        new_dir = self.search_dirs[7]  
                    elif index == 4:
                        new_dir = self.search_dirs[0] 
                    elif index == 5:
                        new_dir = self.search_dirs[1] 
                    elif index == 6:
                        new_dir = self.search_dirs[2] 
                    elif index == 7:
                        new_dir = self.search_dirs[3] 

                    if self.is_within_bounds(x + new_dir[0], y + new_dir[1]) and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == letter:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            self.winner_letter = letter
            self.game_over = True
        else:
            self.game_over = self.is_grid_full()
            if self.game_over:
                self.tie_game = True

    def show_grid(self):
        for row in self.grid:
            print(row)


if __name__ == "__main__":
    g = Grid()
    g.show_grid()