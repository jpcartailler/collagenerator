filename = "sketch_static.png"

def setup():
    size(600, 600)
    noLoop()

def draw():
    background(100)
    strokeWeight(2)
    stroke(255)
    diameter = 30
    angs = [120, 120, 120]
    lastAng = radians(90)
    smooth(4)
    
    imageScale = 50
    imagePadding = imageScale / 2
    cols = width/imageScale
    rows = height/imageScale
    print "cols: " + str(cols)
    print "rows: " + str(rows)
    
    i = 0
    j = 0
    
    while i < cols:
        
        while j < rows: 
            
            print "i,j: " + str(i) + "," + str(j)
    
            x = i*imageScale + imagePadding
            y = j*imageScale + imagePadding
        
            # Change transformation origin to somewhere diff't
            #translate(width/2, height/2)
            #translate(x, y)
            #translate(200,200)
            print "x,y: " + str(x) + "," + str(y)
                
            # colors
        
            count = 0
            for a in angs:
                count += 1
                if count == 1:
                    fill(255, 0, 0)
                elif count == 2:
                    fill(0, 255, 0)
                elif count == 3:
                    fill(0, 0, 255)
                else:
                    fill(100,100,100)
                #arc(width / 2, height / 2, diameter, diameter, lastAng, lastAng + radians(a), PIE)
                arc(x, y, diameter, diameter, lastAng, lastAng + radians(a), PIE)
                lastAng += radians(a)
                
            j += 1
            
        j = 0 # important - Reset the columns, otherwise loop terminates after first column
        i += 1

    save(filename)


