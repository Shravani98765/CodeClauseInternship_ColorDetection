import cv2 as cv
import pandas as pd
import argparse

#CREATING ARGUMENT PARSER TO TAKE THE IMAGE PATH FROM COMMAND LINE
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#PASS THE FILE PATH
img = cv.imread(img_path)

#DECLARING AND INITIALIZING GLOBAL VARIABLES
r = g = b = xpos = ypos = 0
clicked = False

#GETTING DATA FROM CSV FILE AND NAMING COLUMNS OF CSV FILE
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#FUCTION TO GET THE COLOR NAME BY COMPARING RGB VALUES IN CSV FILE
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        #DISTANCE FORMULA: distance = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#FUCTION THAT RETRIEVES THE X AND Y COORDINATES VALUES OF THE COLOR WHERE THE CURSOR CLICKED
def draw_function(event, x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        

        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv.namedWindow('image')
cv.setMouseCallback('image',draw_function)

#THIS FUNCTION ALLOWS USER TO CHECK MULTIPLE COLORS IN THE SAME IMAGE UNTIL ESC KEY IS PRESSED
#IT DISPLAYS THE COLOR NAME AS A TITLEBAR
while(1):

    cv.imshow("image",img)
    if (clicked):
   
        #cv.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #TEXT DISPLAYING THE COLOURS
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv.LINE_AA)

        #FOR LIGHT COLORS WE WILL DISPLAY TEXT IN BLACK 
        if(r+g+b>=600):
            cv.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv.LINE_AA)
            
        clicked=False

    #TO BREAK OUT OF THE LOOP CLICK ESC KEY   
    if cv.waitKey(20) & 0xFF ==27:
        break
    
cv.destroyAllWindows()
