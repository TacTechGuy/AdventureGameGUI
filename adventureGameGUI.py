'''
 /**
 *  Python Final Project
 *  
 *  Project: Game GUI
 *  Using customTKinter, pickle, CTKMessagebox, TKinter  
 * 
 *   Author: Ethan Dechant
 *          
 *  
 *     Date: April 1st, 2025
 *            
 *      Filename: adventureGameGUI.py     
 *   Description: Main file that holds the class for the customGUI
 *                along with all of the methods and variables needed
 *                to run the GUI         
 */
'''
import customtkinter
from CTkMessagebox import CTkMessagebox
import pickle
from PIL import Image, ImageTk
from tkinter import *



storyData = {}
gameLocation = "Intro"
gameIndex = 0
# Setting the inital game item flags
AppleFlag = BowArrowFlag = RopeFlag = KeyFlag = MatchesFlag = True
fightDragonFlag = False
finalPath = 0
inputVal1 = inputVal2 = ""


class customGUI:
  
  def __init__(self):
    #Read from the file first
    global storyData
    storyData = self.readFromFile()

    #inventory = self.getInventory()
    
    # Setup the main GUI window
    self.mainWindow = customtkinter.CTk()
    self.mainWindow.geometry("800x800")
    self.mainWindow.resizable(False, False)

    # Load all of the pictures for the game
    self.bgImage = PhotoImage(file="pictures/main.png")
    self.dragonImage = PhotoImage(file="pictures/dragonOpening.png")
    self.trollBridge = PhotoImage(file="pictures/trollBridge.png")
    self.fairyCaughtBig = PhotoImage(file="pictures/fairyCaughtBig.png")
    self.feedingDragon = PhotoImage(file="pictures/feedingDragonApple.png")
    self.torchForest = PhotoImage(file="pictures/torchForest.png")
    self.endOfDragonRide = PhotoImage(file="pictures/endOfDragonRide.png")
    self.dragonFight = PhotoImage(file="pictures/dragonFight.png")
    self.trollFixBridge = PhotoImage(file="pictures/trollFixBridge.png")
    self.bottomRavine = PhotoImage(file="pictures/bottomRavine.png")
    self.lassoBridge = PhotoImage(file="pictures/lassoBridge.png")
    self.outsideCastle = PhotoImage(file="pictures/outsideCastle.png")
    self.partyReached = PhotoImage(file="pictures/partyReached.png")
    self.partyMissed = PhotoImage(file="pictures/partyMissed.png")
    





    self.myCanvas = Canvas(self.mainWindow, width=800, height=800, highlightthickness=0)
    self.myCanvas.pack(fill="both", expand=True)

    #Set the image
    self.bgMaster = self.myCanvas.create_image(0,0, image=self.bgImage, anchor="nw")
    
    

   
    # Setup a frame for the buttons
    self.bottomFrame = customtkinter.CTkFrame(self.mainWindow)
    self.inventoryFrame = customtkinter.CTkFrame(self.mainWindow)

    self.label1 = self.myCanvas.create_text(400, 50, text="The Adventures of Addie and Speckles", font=("Algerian", 28),fill="brown")

    self.label2 = self.myCanvas.create_text(400, 250, text=storyData["Intro"], font=("Arial Black", 18), width=650, fill="#020302")


    self.startButton = customtkinter.CTkButton(master=self.myCanvas, text="Start Game", command=self.runGame, corner_radius=0)
    self.startButtonWindow = self.myCanvas.create_window(350,700, anchor="nw", window= self.startButton)


    self.mainWindow.title("The Adventure Game")
    self.mainWindow.mainloop()




# //--------------//
# // MAIN PROGRAM //
# //--------------//
  def runGame(self):
    global gameLocation, gameIndex, storyData, finalPath, inputVal1, inputVal2
    global AppleFlag, BowArrowFlag, RopeFlag, KeyFlag, MatchesFlag
    
    # This is where we need to start doing process control, now that the game has started
    # Use this for debugging thins within the game
    # match 
    #     case "Intro":
    #       result = "bla"
    # return result
    if gameLocation == 'Intro' and gameIndex == 0:
      # Now we are at the first scene
        gameLocation = 'Dragon'
    if gameLocation == 'Dragon' and gameIndex == 0:
        self.myCanvas.itemconfig(self.bgMaster, image=self.dragonImage)

        #clear the textbox before we write to it
        self.myCanvas.itemconfig(self.label2, text=storyData["Dragon"])
        self.myCanvas.moveto(self.startButtonWindow, 180, 700)

        # Change the picture
        self.label1Option = customtkinter.CTkLabel(master=self.myCanvas,text="Bow and Arrow",fg_color="green", corner_radius=0)
        self.label1OptionWindow = self.myCanvas.create_window(280, 740, anchor="nw", window=self.label1Option, width= 120)

        self.label2Option = customtkinter.CTkLabel(master=self.myCanvas, text="Apple", fg_color="green", corner_radius=0)
        self.label2OptionWindow = self.myCanvas.create_window(420, 740, anchor="nw", window=self.label2Option, width=120)     

        
        # Add label 
        self.inputBox = customtkinter.CTkEntry(master=self.myCanvas, placeholder_text= "Please enter option", corner_radius=0)
        self.inputBoxWindow = self.myCanvas.create_window(325,700,anchor="nw", window=self.inputBox, width=170)
        

        self.submitButton = customtkinter.CTkButton(master=self.myCanvas, text="Submit", command=self.submission, corner_radius=0)
        self.submitButtonWindow = self.myCanvas.create_window(500, 700, anchor="nw", window=self.submitButton)


        self.startButton.configure(text="Exit Game", command=self.exitGame)
        self.myCanvas.itemconfig(self.label1, text="You are now playing the game")
        self.myCanvas.itemconfig(self.label1, state="hidden")

    # Timeline 1
    if gameLocation == "Feed Dragon" and gameIndex == 1:
        # Change the background image
        self.myCanvas.itemconfig(self.bgMaster, image=self.feedingDragon)

        #Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["Feed Dragon"])

        #Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        #Display the delay message after..
        self.mainWindow.after(8000, self.displayDelayMessage)

    # Timeline 1
    if gameLocation == "Troll Bridge" and gameIndex == 2:
        # Change background
        self.myCanvas.itemconfig(self.bgMaster, image=self.endOfDragonRide)
        #Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["Troll Bridge"])

        # Relabel
        self.label1Option.configure(text="Matches")
        self.label2Option.configure(text="Rope")

    # Timeline 1
    if gameLocation == "AP0-1" and gameIndex == 3:
        self.myCanvas.itemconfig(self.bgMaster, image=self.bottomRavine)
        #Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP0-1"])
        
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        #unpack the frame to hide it
        self.mainWindow.after(10000, self.displayDelayMessage)

    # Timeline 1
    if gameLocation == "AP1-1" and gameIndex == 4:
        self.myCanvas.itemconfig(self.bgMaster, image=self.lassoBridge)
        #Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP1-1"])


        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        #unpack the frame to hide it
        self.mainWindow.after(10000, self.displayDelayMessage)

    # Timeline 1
    if gameLocation == "Across Bridge-1" and gameIndex == 5:
        self.myCanvas.itemconfig(self.bgMaster, image=self.outsideCastle)
        #Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["Across Bridge-1"])
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)
        
        if RopeFlag == False:
            self.label1Option.configure(text="Matches")
            self.label2Option.configure(text="Key")
        elif MatchesFlag == False:
            self.label1Option.configure(text="Bow and Arrow")
            self.label2Option.configure(text="Rope")
    
    # Timeline 1 --> [end] Matches 
    if gameLocation == "AP0-3" and gameIndex == 7:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        self.myCanvas.itemconfig(self.label2, text=storyData["AP0-3"])
   
    # Timeline 1 --> [end] Key
    if gameLocation == "AP1-2" and gameIndex == 8:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        self.myCanvas.itemconfig(self.label2, text=storyData["AP1-2"])
        
    # Timeline 1 --> [end] Bow and Arrow
    if gameLocation == "AP1-3" and gameIndex == 9:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        self.myCanvas.itemconfig(self.label2, text=storyData["AP1-3"])
    
    # Timeline 1 --> [end] Rope
    if gameLocation == "AP0-2" and gameIndex == 6:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        self.myCanvas.itemconfig(self.label2, text=storyData["AP0-2"])
   
    # Timeline 2
    if gameLocation == "Fight Dragon" and gameIndex == 10:
        self.myCanvas.itemconfig(self.bgMaster, image=self.dragonFight)
        global fightDragonFlag
        fightDragonFlag = True
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["Fight Dragon"])
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        # Relabel 
        self.label1Option.configure(text="Matches")
        self.label2Option.configure(text="Rope")

        self.mainWindow.after(100, self.displayDelayMessage)
    
    # Timeline 2 --> matches
    if gameLocation == "AP2-1" and gameIndex == 11:
        # change background
        self.myCanvas.itemconfig(self.bgMaster, image=self.torchForest)

        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-1"])

        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        # Delay before displaying next message
        self.mainWindow.after(10000, self.displayDelayMessage)

    # Timeline 2 --> Rope
    if gameLocation == "AP3-1" and gameIndex == 12:
        self.myCanvas.itemconfig(self.bgMaster, image=self.fairyCaughtBig)    
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP3-1"])
      
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        # Delay before displaying next message
        self.mainWindow.after(17000, self.displayDelayMessage)

    # Timeline 2
    if gameLocation == "AP2-2" and gameIndex == 13:
         # change background
        self.myCanvas.itemconfig(self.bgMaster, image=self.trollBridge)

        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-2"])

        # Relabel 
        self.label1Option.configure(text="Apple")
        self.label2Option.configure(text="Rope")

        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        # Need this fake timer for the pictures to work properly for the events that don't have a timed event following
        self.mainWindow.after(100, self.displayDelayMessage)

    # Timeline 2
    if gameLocation == "AP3-2" and gameIndex == 14:
        # change background
        self.myCanvas.itemconfig(self.bgMaster, image=self.trollBridge)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP3-2"])

        # Relabel
        self.label1Option.configure(text="Matches")
        self.label2Option.configure(text="Apple")

        self.inputBox.delete(0,customtkinter.END) 
    
    # Timeline 2
    if gameLocation == "AP2-3" and gameIndex == 15:
        self.myCanvas.itemconfig(self.bgMaster, image=self.trollFixBridge)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-3"])
    
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        self.mainWindow.after(10000, self.displayDelayMessage)
    
    # Timeline 2
    if gameLocation == "AP2-4" and gameIndex == 16:
        self.myCanvas.itemconfig(self.bgMaster, image=self.lassoBridge)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-4"])

        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        self.mainWindow.after(8000, self.displayDelayMessage)
    
    # Timeline 2
    if gameLocation == "AP3-4" and gameIndex == 17:
        self.myCanvas.itemconfig(self.bgMaster, image=self.bottomRavine)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP3-4"])

        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        self.mainWindow.after(8000, self.displayDelayMessage)

    # Timeline 2
    if gameLocation == "AP3-3" and gameIndex == 18:
        self.myCanvas.itemconfig(self.bgMaster, image=self.trollFixBridge)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP3-3"])
 
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

        self.mainWindow.after(10000, self.displayDelayMessage)

    if gameLocation == "Across Bridge-2" and gameIndex == 19:
        self.myCanvas.itemconfig(self.bgMaster, image=self.outsideCastle)
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["Across Bridge-2"])
        
        # Determine the correct labels for the last scene
        self.finalPathSelection(finalPath)

        # Set the appropriate options
        self.label1Option.configure(text=inputVal1)
        self.label2Option.configure(text=inputVal2)
              
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END) 

    # Timeline 2 --> final key
    if gameLocation == "AP2-5" and gameIndex == 20:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-5"])
         
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)
    
    # Timeline 2 --> final rope
    if gameLocation == "AP2-6" and gameIndex == 21:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-6"])
         
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

    # Timeline 2 --> final apple
    if gameLocation == "AP2-8" and gameIndex == 23:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyMissed)
        self.missedParty()
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP2-8"])
         
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)
    
    # Timeline 2 --> final matches
    if gameLocation == "AP3-5" and gameIndex == 24:
        self.myCanvas.itemconfig(self.bgMaster, image=self.partyReached)
        self.reachedParty()
        # Clear the textBox
        self.myCanvas.itemconfig(self.label2, text=storyData["AP3-5"])
         
        # Clear the entry box
        self.inputBox.delete(0,customtkinter.END)

  # Used to decide what lables to use
  def finalPathSelection(self, data)->str:
    global inputVal1, inputVal2

    match data:
      case 1:
          inputVal1 = "Key",
          inputVal2 = "Rope"
          return
      case 2:
          inputVal1 = "Key"
          inputVal2 = "Apple"
          return
      case 3:
          inputVal1 = "key"
          inputVal2 = "Apple"
          return
      case 4:
          inputVal1 = "Key"
          inputVal2 = "Matches"
          return
    
  def exitGame(self):
    self.mainWindow.destroy()

  def reachedParty(self):
    # Clear the entry box
     self.inputBox.delete(0,customtkinter.END)

     # Lets hide the 2 options along with the entry box and submit button
     self.myCanvas.itemconfig(self.label1OptionWindow, state="hidden")
     self.myCanvas.itemconfig(self.label2OptionWindow, state="hidden")
     self.myCanvas.itemconfig(self.inputBoxWindow, state="hidden")
     self.myCanvas.itemconfig(self.submitButtonWindow, state="hidden")

     # Re-arrange the exit button
     self.myCanvas.moveto(self.startButtonWindow, 350, 700)

     self.myCanvas.itemconfig(self.label1, state="normal")
     self.myCanvas.itemconfig(self.label1, text="You have reached the party!")
  
  def missedParty(self):
    # Clear the entry box
     self.inputBox.delete(0,customtkinter.END)

     # Lets hide the 2 options along with the entry box and submit button
     self.myCanvas.itemconfig(self.label1OptionWindow, state="hidden")
     self.myCanvas.itemconfig(self.label2OptionWindow, state="hidden")
     self.myCanvas.itemconfig(self.inputBoxWindow, state="hidden")
     self.myCanvas.itemconfig(self.submitButtonWindow, state="hidden")

     # Re-arrange the exit button
     self.myCanvas.moveto(self.startButtonWindow, 350, 700)

# //-------------------------------------------//
# // USED FOR HANDLING DELAYS BETWEEN MESSAGES //
# //-------------------------------------------//
  def displayDelayMessage(self):
    global gameLocation, gameIndex
    global fightDragonFlag

    if gameLocation == "Feed Dragon":
      gameLocation = "Troll Bridge"
      gameIndex = 2
      self.runGame()
    
    if gameLocation == "AP0-1" or gameLocation == "AP1-1":
       gameLocation = "Across Bridge-1"
       gameIndex = 5
       self.runGame()
    
    if gameLocation == "AP2-1":
       gameLocation = "AP2-2"
       gameIndex = 13
       self.runGame()

    if gameLocation == "AP3-1":
       gameLocation = "AP3-2"
       gameIndex = 14
       self.runGame()

    if gameLocation == "Fight Dragon" and fightDragonFlag == True:
       gameIndex = 88
       fightDragonFlag = False

    if gameLocation == "AP2-3" or gameLocation == "AP2-4" or gameLocation == "AP3-4" or gameLocation == "AP3-3":
       gameLocation = "Across Bridge-2"
       gameIndex = 19
       self.runGame()

    
    #message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")



# //------------------------------------//
# // HANDLES ALL SUBMIT BUTTON REQUESTS //
# //------------------------------------//
  def submission(self):
    userInput = self.inputBox.get().lower()
    global AppleFlag, BowArrowFlag, RopeFlag, KeyFlag, MatchesFlag
    global fightDragonFlag, finalPath, gameIndex, gameLocation

    # Timeline 1 --> Dragon Scene
    if gameIndex == 0:
      if userInput == "apple":
        #message = CTkMessagebox(title="Information",message=f'Correct input, input value is {userInput}', icon="info")
        gameIndex = 1
        gameLocation = "Feed Dragon"
        AppleFlag = False
        self.runGame()
      elif userInput == "bow and arrow":
        #message = CTkMessagebox(title="Information",message=f'Correct input, input value is {userInput}', icon="info")
        gameIndex = 10
        gameLocation = "Fight Dragon"
        BowArrowFlag = False
        self.runGame()
      else:
        message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
    
    # Timeline 1 --> Troll Bridge
    if gameIndex == 2:
      if userInput == "matches":
        gameIndex = 3
        gameLocation = "AP0-1"
        MatchesFlag = False
        self.runGame()
      elif userInput == "rope":
        gameIndex = 4
        gameLocation = "AP1-1"
        RopeFlag = False
        self.runGame()
      else:
        message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")

    # Timeline 1 -->  Castle Door
    if gameIndex == 5:
        # Matches and key
        if RopeFlag == False:
            if userInput == "matches":
               gameIndex = 7
               gameLocation = "AP0-3"
               MatchesFlag = False
               self.runGame()
            elif userInput == "key":
               gameIndex = 8
               gameLocation = "AP1-2"
               KeyFlag = False
               self.runGame()
            else:
               message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
               
        # Bow/Arrow and rope
        elif MatchesFlag == False:
           if userInput == "bow and arrow":
              gameIndex = 9
              gameLocation = "AP1-3"
              BowArrowFlag = False
              self.runGame()
           elif userInput == "rope":
              gameIndex = 6
              gameLocation = "AP0-2"
              RopeFlag = False
              self.runGame()
           else:
              message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")

    # Timeline 2 -->  Forest
    if gameIndex == 88:
      if userInput == "matches":
          gameIndex = 11
          gameLocation = "AP2-1"
          MatchesFlag = False
          fightDragonFlag = True
          self.runGame()
      elif userInput == "rope":
          gameIndex = 12
          gameLocation = "AP3-1"
          RopeFlag = False
          fightDragonFlag = True
          self.runGame()
      else:
        message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")



    if gameIndex == 13:
       if userInput == "apple":
          finalPath = 1
          gameIndex = 15
          gameLocation = "AP2-3"
          AppleFlag = False
          self.runGame()
       elif userInput == "rope":
          finalPath = 2
          gameIndex = 16
          gameLocation = "AP2-4"
          RopeFlag = False
          self.runGame()
       else:
          message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
    
    if gameIndex == 14:
       if userInput == "matches":
          finalPath = 3
          gameIndex = 17
          gameLocation = "AP3-4"
          MatchesFlag = False
          self.runGame()
       elif userInput == "apple":
          finalPath = 4
          gameIndex = 18
          gameLocation = "AP3-3"
          AppleFlag = False
          self.runGame()
       else:
          message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
    
    if gameIndex == 19:
       if finalPath == 1:
          if userInput == "key":
            gameIndex = 20
            gameLocation = "AP2-5"
            KeyFlag = False
            self.runGame()
          elif userInput == "rope":
            gameIndex = 21
            gameLocation = "AP2-6"
            RopeFlag = False
            self.runGame()
          else:
             message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
       elif finalPath == 2:
          if userInput == "key":
            gameIndex = 20
            gameLocation = "AP2-5"
            KeyFlag = False
            self.runGame()
          elif userInput == "apple":
            gameIndex = 23
            gameLocation = "AP2-8"
            AppleFlag = False
            self.runGame()
          else:
             message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
       elif finalPath == 3:
          if userInput == "key":
             gameIndex = 20
             gameLocation = "AP2-5"
             KeyFlag = False
             self.runGame()
          elif userInput == "apple":
             gameIndex = 23
             gameLocation = "AP2-8"
             AppleFlag = False
             self.runGame()
          else:
             message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
       elif finalPath == 4:
          if userInput == "key":
             gameIndex = 20
             gameLocation = "AP2-5"
             KeyFlag = False
             self.runGame()
          elif userInput == "matches":
             gameIndex = 24
             gameLocation = "AP3-5"
             MatchesFlag = False
             self.runGame()
          else:
             message = CTkMessagebox(title="Information",message="Wrong input please try again", icon="info")
       
          
          
      

# //---------------------------------//
# // READS FROM FILE INTO DICTIONARY //
# //---------------------------------//
  def readFromFile(self):
    #fileStoryData = []

    try:
      # Get the dictionary data from the file  //was StoryFile.txt
      inputFile = open('StoryFile.txt', 'rb')
      inputFileData = pickle.load(inputFile)

      #for data in inputFile:
      #  fileStoryData = data.split('//')
    except IOError:
      
      print('We have an error loading the file')
    #return fileStoryData
    return inputFileData  
  



  def getInventory(self):
    pass


if __name__ == '__main__':
  myGUI = customGUI()
  