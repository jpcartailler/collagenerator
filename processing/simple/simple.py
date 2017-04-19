def setup():
    size(900, 900)
    noLoop()

def draw():
    # Data dictionary
    trimers = ['1-1-1',  '1-1-2',  '1-1-3',  '1-1-4',  '1-1-5',  '1-1-6',  '1-2-2',  '1-2-3',  '1-2-4',  '1-2-5',  '1-2-6',  '1-3-2',  '1-3-3',  '1-3-4',  '1-3-5',  '1-3-6',  '1-4-2',  '1-4-3',  '1-4-4',  '1-4-5',  '1-4-6',  '1-5-2',  '1-5-3',  '1-5-4',  '1-5-5',  '1-5-6',  '1-6-2',  '1-6-3',  '1-6-4',  '1-6-5',  '1-6-6',  '2-2-2',  '2-2-3',  '2-2-4',  '2-2-5',  '2-2-6',  '2-3-3',  '2-3-4',  '2-3-5',  '2-3-6',  '2-4-3',  '2-4-4',  '2-4-5',  '2-4-6',  '2-5-3',  '2-5-4',  '2-5-5',  '2-5-6',  '2-6-3',  '2-6-4',  '2-6-5',  '2-6-6',  '3-3-3',  '3-3-4',  '3-3-5',  '3-3-6',  '3-4-4',  '3-4-5',  '3-4-6',  '3-5-4',  '3-5-5',  '3-5-6',  '3-6-4',  '3-6-5',  '3-6-6',  '4-4-4',  '4-4-5',  '4-4-6',  '4-5-5',  '4-5-6',  '4-6-5',  '4-6-6',  '5-5-5',  '5-5-6',  '5-6-6',  '6-6-6']  
    
    background(60)
    strokeWeight(2)
    stroke(255)
    diameter = 50
    angs = [120, 120, 120]
    lastAng = radians(90)
    smooth(4)
    
    imageScale = 100
    imagePadding = imageScale / 2
    cols = width/imageScale
    rows = height/imageScale
    
    i = 0
    j = 0
    
    trimer_count = 0
    
    while j < rows:
        
        while i < cols:

            # our trimer count will yield the last row
            # as less than a full row, and thus we must end
            # the while early
            trimer_to_draw = list()
            if trimer_count < len(trimers):
                trimer = trimers[trimer_count]
                trimer_to_draw = trimer.split('-')
            else:
                break
            
            trimer_count += 1
    
            x = i*imageScale + imagePadding
            y = j*imageScale + imagePadding
        
            count = 0
            for a in angs:
                count += 1
                if count == 1:
                    rgb = colorize(trimer_to_draw[0])
                    fill(rgb[0], rgb[1], rgb[2])
                    #fill(255, 0, 0)
                elif count == 2:
                    rgb = colorize(trimer_to_draw[1])
                    fill(rgb[0], rgb[1], rgb[2])
                elif count == 3:
                    rgb = colorize(trimer_to_draw[2])
                    fill(rgb[0], rgb[1], rgb[2])
                else:
                    fill(100,100,100)
                arc(x, y, diameter, diameter, lastAng, lastAng + radians(a), PIE)
                lastAng += radians(a)
                
            i += 1
            
        i = 0 # important - Reset the columns, otherwise loop terminates after first column
        j += 1
                
    
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
            
    

