from DrawingPanel import *
P_WIDE = 500   # x value
P_TALL = 400  # y value
P_B_COLOR = "linen"
panel = DrawingPanel(P_WIDE,P_TALL,background=P_B_COLOR)

 


def draw_butterfly():
    # draw 2 wing

    panel.fill_oval(300 + panel.get_mouse_x()*0.1,200 + panel.get_mouse_y()*0.1, 20 ,50,"red")
    panel.fill_oval(320 + panel.get_mouse_x()*0.1,200 + panel.get_mouse_y()*0.1, 20 ,50,"red")

    # draw body
    panel.fill_oval(315+ panel.get_mouse_x()*0.1,205+ panel.get_mouse_y()*0.1, 5 ,40,"black")

def draw_lake():
    panel.fill_oval(20+ P_ADJUST_X,350, P_WIDE/2 ,100,"blue")

def draw_bushes():
    panel.fill_oval(300+ P_ADJUST_X,250+ P_ADJUST_Y, 50 ,90,"green")
    panel.fill_oval(340+ P_ADJUST_X,240+ P_ADJUST_Y, 60 ,150,"dark green")
    panel.fill_oval(380+ P_ADJUST_X,260+ P_ADJUST_Y, 80 ,100,"light green")

def draw_tree():
    # The trunk
    panel.fill_rect(85+80/2-20/2+ P_ADJUST_X,180+ P_ADJUST_Y,20,50,"brown")
    # The leaves
    panel.fill_oval(85+ P_ADJUST_X,80+ P_ADJUST_Y, 80 ,100,"dark green")

def draw_hill():
    panel.fill_oval(0+ P_ADJUST_X,100+ P_ADJUST_Y, 700 ,1000,"green")
    panel.fill_oval(-200+ P_ADJUST_X,80+ P_ADJUST_Y, 700 ,1000,"light green")

def draw_sun():
    panel.fill_oval(450,0, 50 ,50,"yellow")
    
def draw_grass():
    panel.fill_rect(0,P_TALL-100, P_WIDE ,100,"dark green")

def main():
    global P_ADJUST_X,P_ADJUST_Y

    P_ADJUST_X= panel.get_mouse_x()*0.5

    P_ADJUST_Y = panel.get_mouse_y()*0.1

    # clear process
    panel.fill_rect(0,0,P_WIDE,P_TALL,P_B_COLOR)
   
    draw_sun() # not move
    draw_hill()
    draw_butterfly()    
    draw_bushes()
    draw_tree()
    draw_grass() # not move, draw before lake, draw after bushes
    draw_lake()
   

#main()
panel.animate(50,main)
