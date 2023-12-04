from line_ca import Line_clipping
import matplotlib.pyplot as plt
class Polygon(Line_clipping):
    def __init__(self, min: tuple, max:tuple):
        self.x_min = min[0]
        self.y_min=min[1]
        self.x_max=max[0]
        self.y_max=max[1]
        self.x_points = list()
        self.y_points = list()

    def set_vertex(self, point:tuple):
        '''
        point: (x,y) of a vertex'''
        self.x_points.append(point[0])
        self.y_points.append(point[1])

    def clear_vertices(self):
        self.x_points.clear()
        self.y_points.clear()

    
    def get_vertices(self):
        '''
    Prints the x and y coordinates\n
    Returns x_coordinates: List , y_coordinates: List'''
        if len(self.x_points)==0:
            print("\tThere is no points to display!!!\n")
            return "\tThere is no points to display!!!\n"
        print()
        print("X\t Y")
        coords = list()
        for i in range(len(self.x_points)-1):
            print(self.x_points[i],"\t", self.y_points[i])
            coords.append((self.x_points[i], self.y_points[i]))
        return coords
        # return self.x_points, self.y_points
    
    def final_coordinates(self):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        plt.plot(win_x, win_y)

        xs, ys= self.x_points, self.y_points
        xs.append(xs[0])
        ys.append(ys[0])
        self.clipped_xs=list()
        self.clipped_ys=list()

        l=Line_clipping((self.x_min, self.y_min), (self.x_max, self.y_max))
        for i in range(len(xs)-1):
            l.set_line((xs[i],ys[i]),(xs[i+1],ys[i+1]))
            temp_case = l.calc_case()
            clipped_coords = l.final_coordinates(temp_case)
            if len(clipped_coords)==0 or len(clipped_coords)==1:
                continue
            self.clipped_xs.append(clipped_coords[0][0])
            self.clipped_xs.append(clipped_coords[1][0])
            self.clipped_ys.append(clipped_coords[0][1])
            self.clipped_ys.append(clipped_coords[1][1])
            plt.plot([clipped_coords[0][0],clipped_coords[1][0]], [clipped_coords[0][1],clipped_coords[1][1]],c="r")

        # plt.show()
        final_clipped_coords = list()
        for i in range(len(self.clipped_xs)):
            final_clipped_coords.append((self.clipped_xs[i], self.clipped_ys[i]))
        return tuple(final_clipped_coords)

    def draw_unclipped_window(self):
        if len(self.x_points)==0:
            print("\tThere is no points to display!!!\n")
            return
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig= plt.figure()
        plt.plot(win_x, win_y)

        xs, ys= self.x_points, self.y_points
        xs.append(xs[0])
        ys.append(ys[0])
        plt.plot(xs, ys)
        return fig
    def draw_clipped_window(self,new_coords):
        if len(self.x_points)==0:
            print("\tThere is no points to display!!!\n")
            return
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig= plt.figure()
        plt.plot(win_x, win_y)
        new_coords = list(new_coords)
        
        for i in range(0,len(new_coords)-1,2):
            plt.plot([new_coords[i][0], new_coords[i+1][0]], [new_coords[i][1], new_coords[i+1][1]], c="r")
        # plt.show()
        return fig

    def draw_both_window(self, new_coords):
        if len(self.x_points)==0:
            print("\tThere is no points to display!!!\n")
            return
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig= plt.figure()
        plt.subplot(1,2,1)
        plt.plot(win_x, win_y)

        xs, ys= self.x_points, self.y_points
        xs.append(xs[0])
        ys.append(ys[0])
        plt.plot(xs, ys)


        plt.subplot(1,2,2)
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        plt.plot(win_x, win_y)
        new_coords = list(new_coords)
        
        for i in range(0,len(new_coords)-1,2):
            plt.plot([new_coords[i][0], new_coords[i+1][0]], [new_coords[i][1], new_coords[i+1][1]], c="r")
        # plt.show()
        return fig

if __name__ == "__main__":
    p = Polygon((0,0),(100,100))
    # p.set_vertex((-10,10))
    # p.set_vertex((60, 90))
    # p.set_vertex((90, 30))

    # p.set_vertex((-40, 30))
    # p.set_vertex((70, 120))
    # p.set_vertex((70,-30))
    
    # p.set_vertex((20, -20))
    # p.set_vertex((45,125))
    # p.set_vertex((95, -20))
    
    # p.set_vertex((-25, 30))
    # p.set_vertex((50, 140))
    # p.set_vertex((130, 57))
    # p.set_vertex((40, -40))  423,23,3,2,234,2,4,54,32,2,3532,3

    p.set_vertex((423,23))
    p.set_vertex((3,2))
    p.set_vertex((234, 2))
    p.set_vertex((4,54))
    p.set_vertex((32, 2))
    p.set_vertex((352, 3))
    

    # p.clear_lines()
    # print(p.get_vertices())
    new_coords = p.final_coordinates()
    # print(new_coords)
    # p.draw_unclipped_window()
    # p.draw_clipped_window(new_coords)
    p.draw_both_window(new_coords)