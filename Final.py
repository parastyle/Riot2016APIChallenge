import json
import re
from urllib2 import urlopen
from json import load



class summonerId():
    
    def __init__(self):
### Defines all global variables

        self.key = 'insert key here'   
### 
        self.url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'
        self.summonerName = raw_input('Summoner name')
        self.url += self.summonerName
        self.url += self.key
        self.output = urlopen(self.url)
        self.json_obj = load(self.output)
        self.summonerId = self.json_obj[self.summonerName]['id']



class whoAmI():
    
    def __init__(self):
        self.assassin = 0
        self.marksman = 0
        self.fighter = 0
        self.mage = 0
        self.support = 0
        self.tank = 0

        



class masteryByID(summonerId,whoAmI):
    
    def __init__(self):
### Defines all global variables
        self.listOfTuplesWithIdAndPoints = []
        self.identidy = whoAmI()
        self.ids = summonerId()
        self.idTag = idToTag = {1: [u'Mage'], 2: [u'Fighter', u'Tank'], 3: [u'Tank', u'Mage'], 4: [u'Mage'], 5: [u'Fighter', u'Assassin'], 6: [u'Marksman', u'Fighter'], 7: [u'Assassin', u'Mage'], 8: [u'Mage', u'Tank'], 9: [u'Mage', u'Support'], 10: [u'Fighter', u'Support'], 11: [u'Assassin', u'Fighter'], 12: [u'Tank', u'Support'], 13: [u'Mage', u'Fighter'], 14: [u'Tank', u'Fighter'], 15: [u'Marksman'], 16: [u'Support', u'Mage'], 17: [u'Marksman', u'Assassin'], 18: [u'Marksman', u'Assassin'], 19: [u'Fighter', u'Tank'], 20: [u'Support', u'Fighter'], 21: [u'Marksman'], 22: [u'Marksman', u'Support'], 23: [u'Fighter', u'Assassin'], 24: [u'Fighter', u'Assassin'], 25: [u'Mage', u'Support'], 26: [u'Support', u'Mage'], 27: [u'Tank', u'Fighter'], 28: [u'Assassin', u'Mage'], 29: [u'Marksman', u'Assassin'], 30: [u'Mage'], 31: [u'Tank', u'Mage'], 32: [u'Tank', u'Mage'], 33: [u'Tank', u'Fighter'], 34: [u'Mage', u'Support'], 35: [u'Assassin'], 36: [u'Fighter', u'Tank'], 37: [u'Support', u'Mage'], 38: [u'Assassin', u'Mage'], 39: [u'Fighter', u'Assassin'], 40: [u'Support', u'Mage'], 41: [u'Fighter'], 42: [u'Marksman'], 43: [u'Mage', u'Support'], 44: [u'Support', u'Fighter'], 45: [u'Mage'], 48: [u'Fighter', u'Tank'], 50: [u'Mage', u'Fighter'], 51: [u'Marksman'], 53: [u'Tank', u'Fighter'], 54: [u'Tank', u'Fighter'], 55: [u'Assassin', u'Mage'], 56: [u'Assassin', u'Fighter'], 57: [u'Tank', u'Mage'], 58: [u'Fighter', u'Tank'], 59: [u'Tank', u'Fighter'], 60: [u'Mage', u'Fighter'], 61: [u'Mage', u'Support'], 62: [u'Fighter', u'Tank'], 63: [u'Mage'], 64: [u'Fighter', u'Assassin'], 67: [u'Marksman', u'Assassin'], 68: [u'Fighter', u'Mage'], 69: [u'Mage'], 72: [u'Fighter', u'Tank'], 74: [u'Mage', u'Support'], 75: [u'Fighter', u'Tank'], 76: [u'Assassin', u'Fighter'], 77: [u'Fighter', u'Tank'], 78: [u'Tank', u'Fighter'], 79: [u'Fighter', u'Mage'], 80: [u'Fighter', u'Assassin'], 81: [u'Marksman', u'Mage'], 82: [u'Fighter'], 83: [u'Fighter', u'Mage'], 84: [u'Assassin'], 85: [u'Mage', u'Marksman'], 86: [u'Fighter', u'Tank'], 89: [u'Tank', u'Support'], 90: [u'Mage', u'Assassin'], 91: [u'Assassin', u'Fighter'], 92: [u'Fighter', u'Assassin'], 96: [u'Marksman', u'Mage'], 98: [u'Tank', u'Melee'], 99: [u'Mage', u'Support'], 101: [u'Mage', u'Assassin'], 102: [u'Fighter', u'Tank'], 103: [u'Mage', u'Assassin'], 104: [u'Marksman'], 105: [u'Assassin', u'Fighter'], 106: [u'Fighter', u'Tank'], 107: [u'Assassin', u'Fighter'], 110: [u'Marksman', u'Mage'], 111: [u'Tank', u'Fighter'], 112: [u'Mage'], 113: [u'Tank', u'Fighter'], 114: [u'Fighter', u'Assassin'], 115: [u'Mage'], 117: [u'Support', u'Mage'], 119: [u'Marksman'], 120: [u'Fighter', u'Tank'], 121: [u'Assassin', u'Fighter'], 122: [u'Fighter', u'Tank'], 126: [u'Fighter', u'Marksman'], 127: [u'Mage'], 131: [u'Fighter', u'Mage'], 133: [u'Marksman', u'Fighter'], 134: [u'Mage', u'Support'], 136: [u'Mage', u'Figher'], 143: [u'Mage', u'Support'], 150: [u'Fighter', u'Tank'], 154: [u'Tank', u'Fighter'], 157: [u'Fighter', u'Assassin'], 161: [u'Mage'], 201: [u'Support', u'Tank'], 202: [u'Marksman', u'Assassin'], 203: [u'Marksman'], 222: [u'Marksman'], 223: [u'Support', u'Tank'], 236: [u'Marksman'], 238: [u'Assassin', u'Fighter'], 245: [u'Assassin', u'Fighter'], 254: [u'Fighter', u'Assassin'], 266: [u'Fighter', u'Tank'], 267: [u'Support', u'Mage'], 268: [u'Mage', u'Marksman'], 412: [u'Support', u'Fighter'], 420: [u'Fighter', u'Tank'], 421: [u'Fighter'], 429: [u'Marksman'], 432: [u'Support', u'Mage']}

        self.id = self.ids.summonerId
        self.key = '&api_key=59e92af8-207a-4a93-86d3-0bd89050bfbc'   
### 
        self.url = 'https://na.api.pvp.net/championmastery/location/NA1/player/'
        self.url += str(self.id)
        self.url += '/topchampions?count=20'
        self.url += self.key
        self.output = urlopen(self.url)
        self.json_obj = json.load(self.output)

        
        for x in self.json_obj:
            try:
                self.listOfTuplesWithIdAndPoints.append((x['championId'],int((int(x['championPoints']) * float(self.gradeToNumber(x['highestGrade']))) )    ))
            except: 
                self.listOfTuplesWithIdAndPoints.append((x['championId'],x['championPoints']))

        for y in self.listOfTuplesWithIdAndPoints:
            #print self.idTag[y[0]]
            #print y[1]
            if 'Marksman' in self.idTag[y[0]]:
                self.identidy.marksman += y[1]
            if 'Assassin' in self.idTag[y[0]]:
                self.identidy.assassin += y[1]
            if 'Fighter' in self.idTag[y[0]]:
                self.identidy.fighter += y[1]
            if 'Mage' in self.idTag[y[0]]:
                self.identidy.mage += y[1]
            if 'Support' in self.idTag[y[0]]:
                self.identidy.support += y[1]
            if 'Tank' in self.idTag[y[0]]:
                self.identidy.tank += y[1]
        self.whoYouAreList = [self.identidy.assassin,self.identidy.marksman,self.identidy.fighter,self.identidy.mage,self.identidy.support,self.identidy.tank]
        self.Max = self.identidy.assassin
        self.count = 0
        self.index = 0
        for z in self.whoYouAreList:
            if z > self.Max:
                self.index = self.count
                self.Max = z
            self.count += 1   

        if self.index == 0:
            print 'Your true role is assassin'
        elif self.index == 1:
            print 'Your true role is marksman'
        elif self.index == 2:
            print 'Your true role is fighter'
        elif self.index == 3:
            print 'Your true role is mage'
        elif self.index == 4:
            print 'Your true role is support'
        elif self.index == 5:
            print 'Your true role is tank'  
  #idTag is a dict containing   id : [role, role]          

    def gradeToNumber(self,x):
        if x == 'S+':
                return 1.3
        elif x == 'S':
                return 1.2
        elif x == 'A+':
                return 1.1
        elif x =='A':
                return 1
        elif x == 'A-':
                return 0.95
        else:
                return 0.9
            
        
            



class mainClass(masteryByID,whoAmI):
    def __init__(self):
        self.masteryJson = masteryByID()
        self.masteryJson.whoYouAreList
        


x = mainClass()


