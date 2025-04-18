# Phuong Ton Student, CS115 19021, Spring 2025
# Programming Project #2: Motion Parallax , 04/18/2025

# Import module DrawingPanel
# Same folder with motion_parallax.py
from DrawingPanel import *

# PANNEL CONST 
P_WIDE = 500   # x value
P_TALL = 400   # y value
P_B_COLOR = "sky blue"

# OBJECT CONST
WING_BUT_W = 20 
WING_BUT_T = 50

panel = DrawingPanel(P_WIDE,P_TALL,background=P_B_COLOR)

def main():
    # 1. Get mouse position
    per_adjust_x = panel.get_mouse_x()*0.1 
    per_adjust_y = panel.get_mouse_y()*0.05

    # 2. Set up size and position of objects
    # 2.1. Move object
    # Butterfly
    wing_01_x = 300 + per_adjust_x * 2
    wing_01_y = 200 + per_adjust_y * 2
    wing_02_x = 320 + per_adjust_x * 2
    wing_02_y = 200 + per_adjust_y * 2
    wing_w    = 20
    wing_t    = 50
    wing_col  = "red"
    
    body_x    = 315 + per_adjust_x * 2
    body_y    = 205 + per_adjust_y * 2
    body_w    = 5
    body_t    = 40
    body_col  = "black"

    # Lake
    lake_x   = 20  + per_adjust_x
    lake_y   = 350 + per_adjust_y
    lake_w   = P_WIDE/2
    lake_t   = 100
    lake_col = "blue"

    # Bushes
    bush_01_x   = 300 + per_adjust_x
    bush_01_y   = 250 + per_adjust_y
    bush_01_w   = 50
    bush_01_t   = 90
    bush_01_col = "green"
    
    bush_02_x   = 340 + per_adjust_x
    bush_02_y   = 240 + per_adjust_y
    bush_02_w   = 60
    bush_02_t   = 150
    bush_02_col = "sea green"

    bush_03_x   = 380 + per_adjust_x
    bush_03_y   = 260 + per_adjust_y
    bush_03_w   = 80
    bush_03_t   = 100
    bush_03_col = "spring green"

    # Tree
    leaves_x   = 85 + per_adjust_x
    leaves_y   = 80 + per_adjust_y
    leaves_w   = 80
    leaves_t   = 100
    leaves_col = "dark green"
    
    trunk_w    = 20
    trunk_t    = 50
    trunk_x    = 85  + leaves_w/2 - trunk_w/2 + per_adjust_x 
    trunk_y    = 180 + per_adjust_y
    
    trunk_col  = "brown"
    
    # Hill
    hill_01_x   = 0    + per_adjust_x
    hill_01_y   = 100  + per_adjust_y
    hill_w      = 700 
    hill_t      = 1000
    hill_01_col = "OliveDrab1"

    hill_02_x   = -200 + per_adjust_x
    hill_02_y   = 80   + per_adjust_y
    hill_02_col = "yellow green"
    
    # 2.2. None move object
    # Sun
    sun_x   = 450
    sun_y   = 0
    sun_w   = 50
    sun_t   = 50
    sun_col = "yellow"
    
    # Grass
    grass_x   = 0
    grass_y   = P_TALL - 100
    grass_w   = P_WIDE
    grass_t   = 100
    grass_col = "forest green"
        
    # 3. Clear process
    panel.fill_rect(0,0,P_WIDE,P_TALL,P_B_COLOR)

    # 4. Draw objects - draw order top > bottom
    # 4.1. Draw sun
    panel.fill_oval(sun_x, sun_y, sun_w ,sun_t, sun_col)
    
    # 4.2. Draw hill - before tree
    panel.fill_oval(hill_01_x, hill_01_y, hill_w ,hill_t, hill_01_col)
    # hill_02 after hill_01
    panel.fill_oval(hill_02_x, hill_02_y, hill_w ,hill_t, hill_02_col)
       
    # 4.3. Draw tree - after hill
    # The trunk
    panel.fill_rect(trunk_x, trunk_y, trunk_w, trunk_t, trunk_col)
    # The leaves - after trunk
    panel.fill_oval(leaves_x, leaves_y, leaves_w , leaves_t, leaves_col)

    # 4.4. Draw bushes - after hill and before butterfly
    panel.fill_oval(bush_01_x, bush_01_y, bush_01_w, bush_01_t, bush_01_col)
    panel.fill_oval(bush_03_x, bush_03_y, bush_03_w, bush_03_t, bush_03_col)
    # bush 02 - after bust 01 and bush 03
    panel.fill_oval(bush_02_x, bush_02_y, bush_02_w, bush_02_t, bush_02_col)
    # 4.5. Draw butterfly - after hill, bushes, and tree
    # 2 wing - before wing
    panel.fill_oval(wing_01_x, wing_01_y, wing_w , wing_t, wing_col)
    panel.fill_oval(wing_02_x, wing_02_y, wing_w , wing_t, wing_col)
    # body - after wing
    panel.fill_oval(body_x, body_y, body_w ,body_t, body_col)
    
    # 4.6. Draw grass - before lake and after bushes and hills
    panel.fill_rect(grass_x, grass_y, grass_w ,grass_t, grass_col)

    # 4.7. Draw lake - after grass
    panel.fill_oval(lake_x, lake_y, lake_w ,lake_t, lake_col)

#main()
panel.animate(50,main)
