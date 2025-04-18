from DrawingPanel import *
P_WIDTH = 500   # x value
P_LENGTH = 300  # y value
P_B_COLOR = "linen"
myDrawingPannel = DrawingPanel(P_WIDTH,P_LENGTH,background=P_B_COLOR)

def first_draw():
    # (0, 0) is at the window's top-left corner.
    P_WIDTH = 300   # x value
    P_LENGTH = 200  # y value
    
    myDrawingPannel = DrawingPanel(P_WIDTH,P_LENGTH,background="cyan")
    myDrawingPannel.draw_line(0,0,P_WIDTH,P_LENGTH)    
    myDrawingPannel.set_color("red")
    myDrawingPannel.draw_line(P_WIDTH,0,0,P_LENGTH)
    myDrawingPannel.set_stroke(10)
    myDrawingPannel.draw_rect(150-50/2,100-75/2,50,75)
    myDrawingPannel.draw_oval(150-50/2,100-75/2,50,75)

def rect_draw():
    # all your drawing in here
    # clear
    # fill rect with background color
    myDrawingPannel.fill_rect(0,0,P_WIDTH,P_LENGTH,"linen")
    # myDrawingPannel.clear()
    myDrawingPannel.draw_line(0,0,P_WIDTH,P_LENGTH)
    current_x = myDrawingPannel.get_mouse_x()
    current_y = myDrawingPannel.get_mouse_y()
    print(current_x)
    myDrawingPannel.draw_rect(current_x,current_y,P_WIDTH/10,P_LENGTH/10)
    # clear
    # 
def main():
    # clear process
    myDrawingPannel.fill_rect(0,0,P_WIDTH,P_LENGTH,P_B_COLOR)
    current_x = myDrawingPannel.get_mouse_x()
    current_y = myDrawingPannel.get_mouse_y()
    #radius = current_x-P_WIDTH/2
    #myDrawingPannel.draw_oval(P_WIDTH/2-radius,P_LENGTH/2-radius, radius*2 ,radius*2)
    # (current_x - P_WIDTH/2)**2 + (current_y - P_LENGTH/2)**2
    """
    The general equation of a circle is (x - h)² + (y - k)² = r²,
    where (h, k) is the center of the circle and r is the radius. 
    """
    radius = ((current_x - P_WIDTH/2)**2 + (current_y - P_LENGTH/2)**2)**0.5
    myDrawingPannel.draw_oval(P_WIDTH/2-radius,P_LENGTH/2-radius, radius*2 ,radius*2)

myDrawingPannel.animate(50,main) # dynamic call, refesh main
