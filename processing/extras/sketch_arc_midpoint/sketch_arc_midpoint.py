canvas = 400  # set canvas and forget about the rest
diameter = canvas / 13
imageScale = canvas / 9
filename = "sketch_arc_midpoint.png"
background_color = 255


def setup():
    background(background_color)
    x = canvas
    y = canvas
    size(x, y)
    noLoop()

def draw():
    
    # draw big circle (grey)
    arc_x = canvas/2
    arc_y = canvas/2
    arc_h = 200
    arc_w = 200
    arc_start = 0 # radians
    arc_end = radians(315) # radians
    #print "arc_x: " + str(arc_x)
    #print "arc_y: " + str(arc_y)
    fill(200, 200, 200)
    arc(arc_x, arc_y, arc_h, arc_w, arc_start, arc_end, PIE)
    
    
    # draw arc endpoint (gree)
    fill(255)
    #test_x = arc_x + 12.94
    test_x = arc_x + (100 * cos(2 * PI - arc_end))
    test_y = arc_y - (100 * sin(2 * PI - arc_end))
    fill(0, 255, 0)
    ellipse(test_x, test_y, 10, 10)

    
    # draw arc midpoint
    mid_x = (arc_x + test_x) / 2
    mid_y = (arc_y + test_y) / 2
    print "mid_x: " + str(mid_x)
    print "mid_y: " + str(mid_y)
    #ellipse(mid_x, mid_y, 10, 10)
    fill(255, 0, 0)
    arc(mid_x, mid_y,  20, 20, radians(-45), radians(135), OPEN)
    
    save(filename)
