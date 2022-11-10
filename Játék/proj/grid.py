class Grid:
    def __init__(self, pygame):
        self.grid == [[0 for x in range(3)] for y in range(3)]


        self.grid_line = [((0, 200),(600, 200)),
                          ((0, 400)(600, 400)),
                          ((200, 0), (200, 600)),
                          ((400, 0),(400, 600))]

        self.pygame = pygame


    def draw(self, win):
        for line in self.grid_lines:
            self.pygame.draw.line(win, (200, 200, 200), line[0], line[1], 2)

    def show_grid(self):
        for row in self.grid:
            print(row)

    if __name__ == "__main__":
        g = Grid()
        g.show_grid()
