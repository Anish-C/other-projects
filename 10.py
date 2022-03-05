import random
x=random.randint(1,6)
y=random.randint(1,6)
value=x+y
class DiceGame:
    def dice(self,x,y,value):
        self.x=x
        self.y=y
    def dicevalue(self):
        print("Face Value: %s" % value)
    def face(self):
        if x==1:
            print(''' _____
|  o  |
|     |
 _____''')
        elif x==2:
            print(''' _____
| o o |
|     |
 ____''')
        elif x==3:
            print(''' _____
|  oo  |
|   o  |
  _____''')
        elif x==4:
            print(''' _____
| o o |
| o o |
 _______''')
        elif x==5:
            print(''' _____
| o o |
| o o |
|  o  |
  _____''')
        elif x==6:
            print(''' _____
| o o |
| o o |
| o o |
  _____''')
        if y==1:
            print('''_____
|  o  |
|     |
_____''')
        elif y==2:
            print('''_____
| o o |
|     |
____''')
        elif y==3:
            print('''_____
|  oo  |
|   o  |
 _____''')
        elif y==4:
            print('''_____
| o o |
| o o |
_______''')
        elif y==5:
            print('''_____
| o o |
| o o |
|  o  |
 _____''')
        elif y==6:
            print('''_____
| o o |
| o o |
| o o |
 _____''')
      
dice=DiceGame()
dice.dicevalue()
dice.face()
