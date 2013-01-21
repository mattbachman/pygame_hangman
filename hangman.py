# Pygame Hangman
# hangman.py
# mbachman1@gmail.com
# A simple implementaiton of Hangman using python3 and pygame
import pygame
import word
from random import randint

#game variables
wordList=[]
trys=0
wordLength=0
wordIdx=-1
answer=word.word(" ")
complete=False
lost=False
theWords=[]
flashC = 0
isFlash=True

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)


def chooseKey(event):
    key="a"
    if event.key == pygame.K_b:
        key="b"
    if event.key == pygame.K_c:
        key="c"
    if event.key == pygame.K_d:
        key="d"
    if event.key == pygame.K_e:
        key="e"
    if event.key == pygame.K_f:
        key="f"
    if event.key == pygame.K_g:
        key="g"
    if event.key == pygame.K_h:
        key="h"
    if event.key == pygame.K_i:
        key="i"
    if event.key == pygame.K_j:
        key="j"
    if event.key == pygame.K_k:
        key="k"
    if event.key == pygame.K_l:
        key="l"
    if event.key == pygame.K_m:
        key="m"
    if event.key == pygame.K_n:
        key="n"
    if event.key == pygame.K_o:
        key="o"
    if event.key == pygame.K_p:
        key="p"
    if event.key == pygame.K_q:
        key="q"
    if event.key == pygame.K_r:
        key="r"
    if event.key == pygame.K_s:
        key="s"
    if event.key == pygame.K_t:
        key="t"
    if event.key == pygame.K_u:
        key="u"
    if event.key == pygame.K_v:
        key="v"
    if event.key == pygame.K_w:
        key="w"
    if event.key == pygame.K_x:
        key="x"
    if event.key == pygame.K_y:
        key="y"
    if event.key == pygame.K_z:
        key="z"
    return key

def testLost():
    global complete
    global trys
    if (not complete) and (trys==6):
        return True
    return False

def testWord(key):
    global answer
    global trys
    global theWords
    global wordIdx
    pos = theWords[wordIdx].checkLetter(key)
##    print (pos)
##    print(answer.getString())
    if pos[0]==-1:
        trys+=1
        return False
##debug    if answer.checkLetter(key)[0]!=-1:
##        print ("This letter was already entered")
    else:
        answer.addLetter(pos,key)
    if theWords[wordIdx].equals(answer):
        return True
    return False
        

def chooseWord():
    global wordLength
    global answer
    global theWords
    global wordIdx
    global trys
    wordIdx=randint(0,len(theWords)-1)
    #DEBUGprint (wordIdx)
    wordLength=theWords[wordIdx].wordLength
    #DEBUGprint(theWords[wordIdx].getString())
    answer=word.word(" ",True,wordLength)
    trys=0

def drawPost():
    global screen
    global black
    pygame.draw.line(screen,black,(104,295),(200,295),2)#base
    pygame.draw.line(screen,black,(152,295),(152,150),2)#post
    pygame.draw.line(screen,black,(152,150),(195,150),2)#crosspost
    pygame.draw.line(screen,black,(195,150),(195,160),2)#downpost

    
def drawBoard():
    global screen
    global heading
    global font
    global black
    global theWords
    global wordIdx
    global isFlash
    pygame.draw.rect(screen,black,(0,0,600,100),0)
    pygame.draw.rect(screen,black,(0,0,100,500),0)
    pygame.draw.rect(screen,black,(0,400,600,100),0)
    pygame.draw.rect(screen,black,(500,0,100,500),0)
    screen.blit(heading,(300-heading.get_width()//2,10))
    pygame.draw.line(screen,black,(250,100),(250,300),2)
    pygame.draw.line(screen,black,(100,300),(250,300),2)
    screen.blit(font.render("Word Length: "+str(wordLength),True,black),(260,100))
    screen.blit(font.render("Trys Left: "+str(6-trys),True,black),(270,130))
    screen.blit(font.render("Your Word: "+answer.getString(),True,black),(120,320))


    if isFlash and complete:
        screen.blit(font.render("You Won",True,black),(265,280)) 
    elif isFlash and lost:
        screen.blit(font.render("You Lost",True,black),(265,280))
    if wordLength==0 or complete or lost:
        words=font.render("Press n for a new game",True,white)
        screen.blit(words,(300-words.get_width()//2,420))
    drawPost()

def drawPerson(number):
    if number>0:
        pygame.draw.circle(screen, black, (195,170), 10, 1)#head
    if number>1:
        pygame.draw.line(screen,black,(195,180),(195,210),1)#body
    if number>2:
        pygame.draw.line(screen,black,(195,210),(185,230),1)#ll
    if number>3:
        pygame.draw.line(screen,black,(195,210),(205,230),1)#rl
    if number>4:   
        pygame.draw.line(screen,black,(195,195),(180,175),1)#la
    if number>5:
        pygame.draw.line(screen,black,(195,195),(210,175),1)#ra

def buildWords(theList):
    global theWords
    with open('wordsEn.txt','r') as filetxt:
        for line in filetxt:
            for aword in line.split():
                newWord=word.word(aword.strip())
                theWords.append(newWord)

    

buildWords(wordList)
pygame.init()


# Set the width and height of the screen [width,height]
size=[600,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# fonts
font = pygame.font.SysFont("ariel",25)
headFont = pygame.font.SysFont("ariel",90)
heading=headFont.render("Hangman",True,white)



#Loop until the user clicks the close button.
done=False
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
# -------- Main Program Loop -----------

while done==False:
    
    key=""
    #print(wordLength)
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if wordLength==0 or lost or complete:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    chooseWord()
                    complete = False
                    lost= False
        else:
            if event.type == pygame.KEYDOWN:
                key=chooseKey(event)
                #debugprint (key)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
        
            
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    if wordLength>0 and not(key==""):
        complete = testWord(key)
        if not complete:
            lost = testLost()
        
    flashC += 1
    if flashC>1000:
        flashC = 0
    if flashC % 10==0:
        isFlash=not isFlash
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)

    drawBoard()
    if wordLength==0 and not complete and not lost:
        drawPerson(6)
    elif not complete and not lost:
        drawPerson(trys)
        
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

pygame.quit ()
