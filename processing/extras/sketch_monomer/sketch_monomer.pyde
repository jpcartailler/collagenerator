canvas = 100  # set canvas and forget about the rest
diameter = canvas / 13
imageScale = canvas / 9
filename = "sketch_monomer.png"
background_color = 255



def setup():
    background(background_color)
    x = canvas
    y = canvas/2
    size(x, y)
    noLoop()

def draw():
    
    # draw big circle (grey)
    arc_x = canvas/2
    arc_y = canvas/2
    arc_h = 100
    arc_w = 100
    start_angle = 210
    end_angle = start_angle + 120
    arc_start = radians(start_angle) # radians
    arc_end = radians(end_angle) # radians
    #print "arc_x: " + str(arc_x)
    #print "arc_y: " + str(arc_y)

    count = 0
    while (count < 6):
        count = count + 1
        print 'The count is:', count
        
        rgb = colorize(count)
        print(rgb)
        fill(rgb[0], rgb[1], rgb[2])
        arc(arc_x, arc_y, arc_h, arc_w, arc_start, arc_end, PIE)

        filename = "sketch_monomer_" + str(count) + ".png"
        save(filename)
    
    
    
def colorize(chainType):
    
    r = 0
    g = 0
    b = 0
    
    if str(chainType) == str(1):
        # yellow
        r = 255
        g = 255
        b = 0
    elif str(chainType) == str(2):
        # purple
        r = 175
        g = 115
        b = 175
    elif str(chainType) == str(3):
        # red
        r = 255
        g = 0
        b = 0
    elif str(chainType) == str(4):
        # blue
        r = 0
        g = 0
        b = 255
    elif str(chainType) == str(5):
        # green
        r = 0
        g = 255
        b = 0
    elif str(chainType) == str(6):
        # grey
        r = 200
        g = 200
        b = 200
    else:
        # white
        r = 255
        g = 255
        b = 255
        
    rgb = [r, g, b]
    return rgb
            
    

