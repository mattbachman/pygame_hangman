# A word class for hangman
# word.py
# mbachman1@gmail.com
# A class to hold a word for hangman for python


class word(object):
    def __init__(self,aWord,isPlayer=False,length=0):
        self.theWord=[]
        for i in range(len(aWord)):
            self.theWord.append(aWord[i])
        if len(aWord)>0:
            self.wordLength=len(aWord)
        if isPlayer:
            for i in range(length):
                self.theWord.append(" ")
            self.wordLength=length
    def equals(self,wordToCheck):
        if not(wordToCheck.wordLength == self.wordLength):
            return False
        checked = True
        for i in range(self.wordLength):                       
            if not(self.theWord[i] == wordToCheck.theWord[i]):
                checked = False
        return checked

    def addLetter(self,positions,letter):
        for i in range(len(positions)):
            self.theWord[positions[i]]=letter

    def reset(self):
        for i in range(self.wordLength):
            self.theWord.pop()
        self.wordLength=0

    def checkLetter(self,key):
        positions=[]
        checked = False
        for i in range(self.wordLength):
            if key==self.theWord[i]:
                positions.append(i)
                checked = True
        if not checked:
            positions.append(-1)

        return positions

    def getString(self):
        aS=""
        for i in range(self.wordLength):
            aS+=self.theWord[i]
        return aS
            
