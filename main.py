#i'm going to start learing about ML/AI on my own via youtube and all of that fun stuff (11-25-23)
#numpy will be used for a majority of the math
#a good portion of this is going to be finding and parsing data to use
import numpy as np
import pyautogui as pag
import subprocess as sp
import cv2
import pytesseract as pytes
from ewmh import EWMH
import datetime, time, threading, re, json
print('[',datetime.datetime.now(),']','Program is Running...')
#i picked a game that i want to make an ai for, i want to try and make an ai that can play Tunic.
#DOING PMD instead with pyboy
#pyboy is a tool that bas functionality for AI and all that stuff :)
#it only supports gb and gbc rn :(

#dictionary of the personality questions <"question",["options"]>
personality ={
    "A test is coming up. how do you study for it?":["Study Hard","At the last seccond","ignore it and play"],
    "Can you focus on somthing you like?":["yes","no"],
    "There is a bucket. if you put water in it, how high will you fill it?":["Full","half","a Little"],
    "If you are offered a choice of two gifts. Which do you take?":["Big Box","Small Box"],
    "You broke a rotten egg in your room! What will you do?":["Open a window right away.","Take a sniff first."],
    "A friend brought something you've forgotten, how do you thank them":["say thank you regularly.","say thanks with a joke.","say thanks but be cool."],
    "There is a wallet at the side of a road.":["Turn it in to the police","Yay!Yay!","Is anyone watching?"],
    "You're going bungee jumping for the first time. Since it's scary, you decide to test the jump with a doll... And the bungee cord snaps! Will you still try to make a jump anyway?":["yes","no"],
    "There is an alien invasion! What will you do?":[["Fight",{'You valiantly fight the aliens... But, you are defeated... An alien says to you... "YOU HAVE IMPRESSED US. IT WAS A PLEASURE TO SEE. JOIN US, AND TOGETHER WE SHALL RULE THE WORLD." What will you do?':['Rule with the aliens','Refuse']}],"Run","Ignore it"],#if you select FIGHT there is a seccond part to the question
    "There is a scream from behind a door! How will you react?":["Yank the door open","Scream in unison"],
    "A delinquent is hassling a girl on a busy city street! What will you do?":["Help without hesitation","Help, even if scared","Call the police","Do nothing out of fear"],
    "Are you a cheerful personality?":["yes","No"],
    "Do you like to noisily enjoy yourself with others?":["yes","no"],#what a weird way to say it lol
    "Its the summer holliday, Where do you wish to go?":["the beach","the spa","anywhere"],
    "A foreign person has started up a conversation with you. To be honest, you don't have a clue what this fellow is saying. How do you reply?":["Haha! yes very funny","Um... could you say that again?","Right... well i gotta go"],
    "have you ever made a pitfall trap":["yes","no"],
    "Do you like pranks?":["yes","no"],
    "are there many things that you would like to do?":["yes","no"],
    "your friend is being bullied what do you do?":["Face up to the bully","Caution the bully from afar","heckle the bully from behind"],
    "Do you like groan-inducing puns?":["Love them!","A little","Spare me"],
    "Do you tend to laugh a lot?":["yes","no"],
    "Do others often call you childish?":["yes","no"],
    "Do you like to imagine things for your amusement?":["yes","no"],
    "A human hand extends out of the toilet. What do you do?":["Scream and run","close the lid without a word","Shake hands with it"],
    "Grab any digit on your left hand with your right, which finger do you grab?":["Thumb","Index Finger","middle finger","ring finger","little finger"],
    "You are suddenly locked in a pitch black room, what do you do?":["Kick the door","cry","clean it"],
    "can you go into a haunted house?":["No Problem!","Uh...N-no...","With somone i like"],
    "You receive a gift! But you don't know what's in it. You're curious, so what do you do?":["open it now.","open it later.","Get somone to open it."],
    "You win the lottery, what do you do with the money?":["Spend it now.","Save it","give it away"],
    "you come across a treasure chest, what do you do?":["open it right away","No... could be a trap...","Its going to be empty..."],
    "Your friend fails to show up at a meeting on the promised time, what do you do?":["Become Irritated","Wait patiently","Get angy and bail"],
    "Your country leader is in front of you how do you speak to them?":["speak calmly","Speak nervous","WHATEVER!!"],
    "Do you tell others to watch what they say?":["yes","no"],
    "Do you think you are cool? Be honest.":["yes","no"],
    "Can you sincerely thank somone when you feel greatful?":["yes","no"],
    "Do you occasionally coinsider yourself dull or overly cautious?":["yes","no"],
    "Do you dream of lounging around idly without much excitement?":["yes","no"],
    "Do you like to fight?":["yes","no"],
    "Do you often yawn?":["yes","no"],
    "Are you often late for school or meetings?":["yes","no"],
    "Do you get the feeling that you have slowed down recently?":["yes","no"],
    "It's a pleasant day at the beach, how do you feel?":["this feels great","Snore...","i want to go home soon"],
    "Do you fall asleep without noticing?":["yes","no"],
    "Do you feel lonesome when you are alone?":["yes",'no'],
    "Do you hate to be the last person to leave class at the end of the day?":["yes","no"],
    "What do you do with your room lights when you are going to bed at night?":["leave it on.","turn it off"],
    "It's a weekend but no one will play with you, what do you do?":["go on a trip","hang around vacantly","huddle in a corner"], #Eat ass and smoke grass
    "Do you sometimes run out of things to do all of the sudden?":["yes","no"],
    "How quick do you respond to an email?":["right away!","May reply, may not.","Too much trouble"],
    "there is a person you like but no oportunity to get close. what do you do?":["Bravly declare my love","Might say hello...","pull a prank to get attention","look from afar"],
    "The road forks left and right you are told there is treasure on the right. what do you do?":["instanty go right","its a trap, go left","choose either side"],
    "On vacation outings, you want to...":["go alone","go with others"],
    "its the summer festival! Do you like carnivals?":["Love them!","Don't care"],
    'Sombody calls you "weird but funny." How does that make you feel?':["Happy!","Not Happy."],
    "Are you a boy or a girl?":["Male","Female"] # :(
}

#defining GBA controls as functions to make it easier to read
#also bc this is kinda rudamentrary it makes it easier to change how they work later when im not being lazy
def up():
    pag.press('up')
def right():
    pag.press('right')
def down():
    pag.press('down')
def left():
    pag.press('left')
def a():
    pag.press('x')
def b():
    pag.press('z')
def start():
    pag.press('enter')
def select():
    pag.press('backspace')
def lTrig():
    pag.press('a')
def rTrig():
    pag.press('s')
#hold key
def holdUp(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('up')
def holdRight(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('right')
def holdDown(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('down')
def holdLeft(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('left')
def holdA(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('x')
def holdB(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('z')
def holdStart(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('enter')
def holdSelect(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('backspace')
def holdLTrig(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('a')
def holdRTrig(duration):
    start = time.time()
    while time.time() - start < duration: #hold key for duration
        pag.press('s')


def removeNonWords(text): #NOT FULLY IMPLIMENTED
    return re.sub(r"[^\w]", "", text)

#instance thee class
ewmh = EWMH()
def getGBAWindowInfo():
    # Get a list of all visible windows
    all_windows = ewmh.getClientList()

    # Define the title or other identifying information of the mGBA window
    mGBA_window_title = "mGBA"

    # Search for the mGBA window in the list of all windows
    for window in all_windows:
        if mGBA_window_title == window.get_wm_name():
            mGBA_window = window
            return mGBA_window
GameName = "PMDRRT.gba"
def runMGBA():
    #mGBA with PMD final decision
    print('[',datetime.datetime.now(),']','Running %s'% (GameName))
    sp.run(['mgba','-7','SL1/PMD-AI-ML-PROJECT/%s'%(GameName)],stdin=sp.PIPE,text=True)
    
#this should swap to mGBA
def swapToMGBA():
    #print(ewmh.getClientList())
    clList = ewmh.getClientList()
    for Window in clList:
        #print("Visible Name:",ewmh.getWmVisibleName(Window),"\nName:",ewmh.getWmName(Window),"\nPID:",ewmh.getWmPid(Window))
        if ewmh.getWmName(Window) == "b'mGBA'":
            ewmh.setActiveWindow(Window)
            ewmh.display.flush()
            location = pag.locateAllOnScreen("SL1/PMD-AI-ML-PROJECT/imgs/Safe-StartupScreen.png",confidence=0.7)
            pag.moveTo(pag.center(location))
            print('move to..')
            pag.click(pag.center(location))
            print('click...')
            print('[',datetime.datetime.now(),']','%s active'% (GameName))
            if (location):
                print(location)
                return location

#test controls
def testController():
    pag.sleep(3   )
    with pag.hold('z'):
        pag.press(['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'])
        print("x spam while holding z run")
    pag.sleep(4)
    pag.press(['enter','enter','enter','enter','enter','enter'])
    print('enter,enter,enter....')

def StartUp():
    json_handler()
    while (str(ewmh.getWmName(ewmh.getActiveWindow())) != "b'mGBA'"):
        print('waiting for emulator and/or rom...') #if you are having issues here, either mgba is not booting or you do not have the rom, or it is not named correctly.
        #print(ewmh.getWmName(ewmh.getActiveWindow()))
        swapToMGBA()
    ScreenLocation = swapToMGBA()
    print("Screen Location:",ScreenLocation)
    print('set to mGBA')
    testTrl.start()
    testTrl.join()
    playGame.start()
    playGame.join()

def GetVP():
    time.sleep(1)
    try:
        ViewPort = list(pag.locateAllOnScreen("SL1/PMD-AI-ML-PROJECT/imgs/Safe-StartupScreen.png",confidence=0.9))
        return ViewPort
    except:
        time.sleep(1)
        try:
            ViewPort = list(pag.locateAllOnScreen("SL1/PMD-AI-ML-PROJECT/imgs/Safe-StartupScreen.png",confidence=0.8))
            return ViewPort
        except:
            time.sleep(1)
            try:
                ViewPort = list(pag.locateAllOnScreen("SL1/PMD-AI-ML-PROJECT/imgs/Safe-StartupScreen.png",confidence=0.7))
                return ViewPort
            except:
                time.sleep(1)
                try:
                    ViewPort = list(pag.locateAllOnScreen("SL1/PMD-AI-ML-PROJECT/imgs/Safe-StartupScreen.png",confidence=0.6))
                    return ViewPort
                except:
                    print("Can't find ViewPort...\nexiting...")
                    exit()

def ImageOnScreen(file,confidence):
    temp = None
    try:
        temp = pag.locateOnWindow(file,'mGBA',grayscale=False,confidence=confidence)
    except:
        return False
    if temp == None:
        return False
    else:
        return True
    
#json handler that stores inputs given situations, player data (e.g. Healh, inventory, moves, which charachter)
def json_handler():
    Rank = {
        "Rank":{
            "RankName":"bronze",
            "RankXP":0
        }
    }
    GameState={
        "GameState":"CutScene" #either CutScene, Overworld, or Dungeon
    }
    TeamData = { 
        "Team1":{
            "member-1":{
                "pokemon":"",
                "move-1":"",
                "move-2":"",
                "move-3":"",
                "move-4":"",
                "held-item":"",
                "HP":0,              #https://bulbapedia.bulbagarden.net/wiki/Stat_(Mystery_Dungeon)#Stats
                "max-HP":0,        
                "Attack":0,
                "Defense":0,
                "SP-Attack":0,
                "SP-Defense":0,
                "Speed": 0, #never actually used for gameplay, the stat does nothing in any of the PMD games until super PMD where the stat is used to increase accuracy
                "Travel-Speed":0, #on a scale of +/-5  afflictions that effect speed are coinsidered status effects in PMD RRT and only make you move/have an action more or less each turn.
                "Belly":100, #Defaults to 100 at the start of a Dungeon and goes down from there.
                "Stat-mods":{ # on a +/-10 scale with each following a percentage multiplier, these reset when a Pokémon leaves a dungeon, advances a floor, or steps on a Wonder Tile.
                    "HP":0,
                    "Attack":0,
                    "Defense":0,
                    "SP-Attack":0,
                    "SP-Defense":0,
                    "Speed": 0
                }
            },
            "member-2":{
                "pokemon":"",
                "move-1":"",
                "move-2":"",
                "move-3":"",
                "move-4":"",
                "held-item":"",
                "HP":0,
                "max-HP":0,        #https://bulbapedia.bulbagarden.net/wiki/Stat_(Mystery_Dungeon)#Stats
                "Attack":0,
                "Defense":0,
                "SP-Attack":0,
                "SP-Defense":0,
                "Speed": 0, #never actually used for gameplay, the stat does nothing in any of the PMD games until super PMD where the stat is used to increase accuracy
                "Travel-Speed":0, #on a scale of +/-5  afflictions that effect speed are coinsidered status effects in PMD RRT and only make you move/have an action more or less each turn.
                "Belly":100, #Defaults to 100 at the start of a Dungeon and goes down from there.
                "Stat-mods":{ # on a +/-10 scale with each following a percentage multiplier, these reset when a Pokémon leaves a dungeon, advances a floor, or steps on a Wonder Tile.
                    "HP":0,
                    "Attack":0,
                    "Defense":0,
                    "SP-Attack":0,
                    "SP-Defense":0,
                    "Speed": 0
                }
            },
            "member-3":{
                "pokemon":"",
                "move-1":"",
                "move-2":"",
                "move-3":"",
                "move-4":"",
                "held-item":"",
                "HP":0,
                "max-HP":0,        #https://bulbapedia.bulbagarden.net/wiki/Stat_(Mystery_Dungeon)#Stats
                "Attack":0,
                "Defense":0,
                "SP-Attack":0,
                "SP-Defense":0,
                "Speed": 0, #never actually used for gameplay, the stat does nothing in any of the PMD games until super PMD where the stat is used to increase accuracy
                "Travel-Speed":0, #on a scale of +/-5  afflictions that effect speed are coinsidered status effects in PMD RRT and only make you move/have an action more or less each turn.
                "Belly":100, #Defaults to 100 at the start of a Dungeon and goes down from there.
                "Stat-mods":{ # on a +/-10 scale with each following a percentage multiplier, these reset when a Pokémon leaves a dungeon, advances a floor, or steps on a Wonder Tile.
                    "HP":0,
                    "Attack":0,
                    "Defense":0,
                    "SP-Attack":0,
                    "SP-Defense":0,
                    "Speed": 0
                }
            }
        }
    }
    ToolBox = {
        "ItemsHeld":0,
        "Max-Capacity":20,
        "Items":{
            #item:description,

        }
    }
    Kangaskhan = {
        "Items":{ #can store up to 999 of each item in game in Red Rescue Team.
            #item:description, 
        }
    }
    Persian = {
        "money":0
    }
    Missions = {
        'Name':{
            'Place':"",
            'Floor':"",
            'Task':"",
            'Type':"" #A B C D ...
        }
    }
    with open("SL1/PMD-AI-ML-PROJECT/Data/rank.json","w") as r:
        json.dump(json.dumps(Rank),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/bank.json","w") as r:
        json.dump(json.dumps(Persian),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/ibank.json","w") as r:
        json.dump(json.dumps(Kangaskhan),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/missions.json","w") as r:
        json.dump(json.dumps(Missions),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/toolbox.json","w") as r:
        json.dump(json.dumps(ToolBox),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/teams.json","w") as r:
        json.dump(json.dumps(TeamData),r)
    with open("SL1/PMD-AI-ML-PROJECT/Data/GSball.json","w") as r:
        json.dump(json.dumps(GameState),r)

#AI input handler, this should make decisions on the data stored by the json handler
def Player_Input():
    NotImplemented #yet

#ViewPort
def ViewPort_and_imageProcessing():
    #ViewPort
    VPList = list(ViewPort[0]) #[top,left,Width,Height]
    TrueVP = [list(pag.center(ViewPort[0]))[0]-VPList[2]/2,list(pag.center(ViewPort[0]))[1]-VPList[3]/2,VPList[2],VPList[3]] 
    desired_width = 400
    cv2.namedWindow('ViewPort',cv2.WINDOW_NORMAL)
    while True:
        screen = pag.screenshot(region=(int(TrueVP[0]),int(TrueVP[1]),int(TrueVP[2]),int(TrueVP[3])))
        screen = np.array(screen) #bbox = left, top, right, bottom
        processer = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) #make gray
        screen = cv2.threshold(processer, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] #add a threshhold for visablility
        #screen = 255 - screen
        aspect_ratio = screen.shape[1] / screen.shape[0]
        desired_height = int(desired_width / aspect_ratio)
        TxtOnScreen = pytes.image_to_string(screen,config="--psm 11",lang="eng").strip() #--psm 11, works ok
        print(TxtOnScreen)
        cv2.imshow('ViewPort',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
        swapToMGBA()
        cv2.resizeWindow('ViewPort',desired_width,desired_height)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        

#threads
RunEmu = threading.Thread(target=runMGBA)
#SwapToEmu = threading.Thread(target=swapToMGBA)
startUp = threading.Thread(target=StartUp)
testTrl = threading.Thread(target=testController)
playGame = threading.Thread(target=ViewPort_and_imageProcessing)

#start threads
RunEmu.start()
ViewPort = GetVP()
startUp.start()

#end threads
startUp.join()
RunEmu.join()


print('[',datetime.datetime.now(),']','Program Stopped...')


