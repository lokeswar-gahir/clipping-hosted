from point_ca import Point_clipping
import matplotlib.pyplot as plt

class Line_clipping(Point_clipping):
    def __init__(self,min:tuple, max:tuple):
        super().__init__(min, max)
        self.p1 = None
        self.p2 = None

    def set_line(self, p1, p2):
        '''
        This function sets only one line at a single call.'''
        self.p1 = p1
        self.p2 = p2
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        try:
            self.slope = (self.y2-self.y1)/(self.x2-self.x1)
        except ZeroDivisionError:
            self.slope = "inf"
    
    def TBRL_code(self,coord:tuple):
        x = coord[0]
        y = coord[1]
        TBRL=[0,0,0,0]
        if x<self.x_min:
            TBRL[3]=1
        if y<self.y_min:
            TBRL[1]=1
        if y>self.y_max:
            TBRL[0]=1
        if x>self.x_max:
            TBRL[2]=1
        return "".join(list(map(str,TBRL)))
    
    def calc_case(self):
        '''
        Returns 0: if not visible
        Returns 1: if visible
        Returns 2: if clipping case
        '''
        x1_y1_code_int = int(self.TBRL_code(self.p1), 2)
        x2_y2_code_int = int(self.TBRL_code(self.p2), 2)
        if (x1_y1_code_int | x2_y2_code_int) == 0:
            # self.show_line()
            return 1
        elif (x1_y1_code_int==0 and x2_y2_code_int!=0) or (x1_y1_code_int!=0 and x2_y2_code_int==0):
            return 2
        return 0
    
    def final_coordinates(self, case):
        # if case==0:
        #     return (0,0), (0,0)
        if case==1:
            return self.get_line()
        else:
            return self.get_cliped_line()

    def top(self):
        if self.slope == 0:
            return None
        y=self.y_max
        if self.slope == "inf":
            x = self.x1
            return round(x,4),round(y,4)
        if max(self.y1, self.y2)<=self.y_max:
            y = max(self.y1, self.y2)
        x = self.x1+((y-self.y1)/self.slope)
        return round(x,4),round(y,4)

    def bottom(self):
        # if self.slope== "inf":
        #     x = self.x1
        #     return round(x,4),round(y,4)
        # if self.slope == 0:
        #     return None
        # y=self.y_min          
        # x = self.x1+((y-self.y1)/self.slope)
        # return round(x,4),round(y,4)

        if self.slope == 0:
            return None
        y=self.y_min
        if self.slope == "inf":
            x = self.x1
            return round(x,4),round(y,4)
        if min(self.y1, self.y2)>=self.y_min:
            y = min(self.y1, self.y2)
        x = self.x1+((y-self.y1)/self.slope)
        return round(x,4),round(y,4)
    
    def left(self):
        if self.slope == "inf":
            return None
        x=self.x_min
        if min(self.x1, self.x2)>=self.x_min:
            x = min(self.x1, self.x2)
        y= self.y1+((x-self.x1)*self.slope)
        return round(x,4),round(y,4)
    
    def right(self):
        if self.slope == "inf":
            return None
        x=self.x_max
        if max(self.x1, self.x2)<=self.x_max:
            x = max(self.x1, self.x2)
        y= self.y1+((x-self.x1)*self.slope)
        return round(x,4),round(y,4)
    
    def get_line(self):
        if self.p1 is not None:
            print(f"Line is visible :\n\t{self.p1}, {self.p2}")
            return self.p1, self.p2
        return "\tNo line is set to display.\n\tTry setting the line using set_line function."

    def get_cliped_line(self):
        top = self.top()
        bottom = self.bottom()
        left = self.left()
        right = self.right()
        
        is_top = super().check(top)
        is_bottom = super().check(bottom)
        is_left = super().check(left)
        is_right = super().check(right)
        if top==0 and bottom ==0 and left==0 and right==0:
            print("There is nothing to display.")
            return
        
        print("The coordinates are:")
        final_coords = list()
        
        if is_bottom:
            print("\tBottom:",bottom)
            if bottom not in final_coords:
                final_coords.append(bottom)
        if is_left:
            print("\tLeft:",left)
            if left not in final_coords:
                final_coords.append(left)
        if is_right:
            print("\tRight:",self.right())
            if right not in final_coords:
                final_coords.append(right)
        if is_top:
            print("\tTop:",top)
            if top not in final_coords:
                final_coords.append(top)
        
        return tuple(final_coords)

    def draw_unclipped_window(self):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig, ax = plt.subplots()
        ax.plot(win_x, win_y)

        if self.p1 is not None:
            ax.plot([self.x1, self.x2], [self.y1, self.y2])
        return fig
    
    def draw_clipped_window(self, new_coords):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        # fig, ax = plt.subplots()
        fig= plt.figure()
        plt.plot(win_x, win_y)
        plt.plot([new_coords[0][0], new_coords[1][0]], [new_coords[0][1], new_coords[1][1]])
        return fig

    def draw_both_window(self, new_coords):
        win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
        win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
        fig = plt.figure()
        plt.subplot(1,2,1)
        plt.plot(win_x, win_y)
        if self.p1 is not None:
            plt.plot([self.x1, self.x2], [self.y1, self.y2])

        plt.subplot(1,2,2)
        plt.plot(win_x, win_y)
        if len(new_coords)==2:
            win_x = [self.x_min, self.x_max, self.x_max, self.x_min, self.x_min]
            win_y = [self.y_min, self.y_min, self.y_max, self.y_max, self.y_min]
            
            plt.plot([new_coords[0][0], new_coords[1][0]], [new_coords[0][1], new_coords[1][1]])
        # plt.show()
        return fig


if __name__ == "__main__":
    # window = list(map(str.strip,input("Enter the window size(x_min, y_min, x_max, y_max): ").split(",")))
    # while len(window) != 4:
    #     print("\tEnter 4 valid coordinates!!!")
    #     window = list(map(str.strip,input("Enter the window size(x_min, y_min, x_max, y_max): ").split(",")))
    # window = list(map(float, window))
    # bottom_left = (window[0], window[1])
    # top_right = (window[2], window[3])

    # line = list(map(str.strip,input("Enter the line coordinates(x1, y1, x2, y2): ").split(",")))
    # while len(line) != 4:
    #     print("\tEnter 4 valid coordinates!!!")
    #     line = list(map(str.strip,input("Enter the window size(x1, y1, x2, y2): ").split(",")))
    # line = list(map(float, line))
    # p1 = (line[0], line[1])
    # p2 = (line[2], line[3])


    # l = Line_clipping(bottom_left,top_right)
    # l.set_line(p1,p2)
    # case = l.calc_case()
    # new_coords = l.final_coordinates(case)
    # # l.draw_unclipped_window()
    # l.draw_both_window(new_coords)

    l = Line_clipping((0,0),(100,100))
    # l.set_line((-10,-10),(50,70))
    # l.set_line((-10,-10),(60,90))
    # l.set_line((90,30),(-10,-10))
    l.set_line((12, 12),(129,165))  #12,12,129,165
    case = l.calc_case()
    new_coords = l.final_coordinates(case)
    print(new_coords)
    # l.draw_unclipped_window()
    l.draw_both_window(new_coords)

    # print(l.window_coordinates())
    # print(l.check((3,10), (3,23)))
    # print(l.TBRL_code((28,18)))
    # print(l.show_case((-2,-2), (28,18)))
