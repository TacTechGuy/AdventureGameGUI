
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
 *      Filename: fileWrite.py     
 *   Description: Used to update the StoryFile.txt after 
 *                updating the sentences file, so the input
 *                for the game data will be a dictionary, 
 *                inventory items will most likely be a list.         
 */
'''
import pickle

def main():
    # Events for the timeline
    timeLine = ["Intro", "Dragon", "Feed Dragon", "Troll Bridge", "AP0-1", "AP1-1", "Across Bridge-1", "AP0-2", "AP1-2", 
                "AP0-3","AP1-3", "Fight Dragon", "AP2-1", "AP3-1", "AP2-2", "AP3-2", "AP2-3", "AP2-4", "AP3-3", "AP3-4", 
                "Across Bridge-2","AP2-5", "AP2-6", "AP2-7", "AP2-8", "AP3-5", "AP3-6", "AP3-7", "AP3-8"]

    # First read from the file
    rawSentences = open('sentences.txt', 'r')
    sentences = []

    getline = rawSentences.readline().strip()

    while getline != '':
        sentences.append(getline)
        getline = rawSentences.readline().strip()


    rawSentences.close()
    # for data in rawSentences:
    #     sentences = data.split('//')

    # Combine into a dictionary
    fullSentence = {k:v for k, v in zip(timeLine, sentences)}

    print(fullSentence)

    outputFile = open('StoryFile.txt', 'wb')
    
    # Now lets write the data to the file 
    pickle.dump(fullSentence, outputFile )

    outputFile.close()

    # Read from the file and output to the terminal
    inputFile = open('StoryFile.txt', 'rb')
    inputData = pickle.load(inputFile)
    
    print('Reading Dictionary from file...')

    # Print out the dictionary with keys and values organized
    
    for key in inputData:
        print(f'Key: {key} Value: {inputData[key]}')

    # Close the file
    inputFile.close()



if __name__ == '__main__':
    main()