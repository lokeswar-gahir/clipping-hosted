import matplotlib.pyplot as plt
class Point_clipping:
    def __init__(self,min:tuple,max:tuple):
        self.x_min = min[0]
        self.x_max=max[0]
        self.y_min=min[1]
        self.y_max=max[1]
        self.x=None
        self.y=None
    def window_coordinates(self):
        return f"""
    x_min : {self.x_min}
    y_min : {self.y_min}
    x_max : {self.x_max}
    y_max : {self.y_max}
"""
    def check(self, coord):
        if coord is not None:
            self.x=coord[0]
            self.y=coord[1]
            if (self.x_min<= coord[0] <= self.x_max) and (self.y_min<= coord[1] <= self.y_max):
                return 1
        return 0
    def draw_unclipped_window(self):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig, ax = plt.subplots()
        ax.plot(win_x, win_y)

        if self.x is not None:
            ax.scatter([self.x], [self.y])
        return fig
    def draw_clipped_window(self, coord):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig, ax = plt.subplots()
        ax.plot(win_x, win_y)
        if self.check(coord)==1:
            ax.scatter([self.x], [self.y])
        return fig
    
    def draw_both_window(self, coord):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig = plt.figure()
        plt.subplot(1,2,1)
        plt.plot(win_x, win_y)
        if self.x is not None:
            plt.scatter([self.x], [self.y])

        plt.subplot(1,2,2)
        plt.plot(win_x, win_y)
        if self.check(coord)==1:
            plt.scatter([self.x], [self.y])
        return fig
if __name__ == "__main__":
    x,y=tuple(map(int,input("Enter the coordinates: ").split(",")))
    p = Point_clipping(0,0,53,23)
    print(p.window_coordinates())