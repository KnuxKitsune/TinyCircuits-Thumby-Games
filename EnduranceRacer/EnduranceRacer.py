#### !!!! BLOCKLY EXPORT !!!! ####
from thumbySprite import Sprite
from thumbyGraphics import display
import thumbyButton as buttons
import time
import random
Number = int

Title = None
Player = None
Enemy = None
Enemy2 = None
ScoreName = None
GetReady = None
sprDigits = None
Time = None
Score = None
i = None
r = None
num = None

Title = Sprite(1,1,bytearray([1]))

Player = Sprite(1,1,bytearray([1]))

Enemy = Sprite(1,1,bytearray([1]))

Enemy2 = Sprite(1,1,bytearray([1]))

ScoreName = Sprite(1,1,bytearray([1]))

GetReady = Sprite(1,1,bytearray([1]))

sprDigits = Sprite(1,1,bytearray([1]))

def __print_to_display__(message):
      message = str(message)
      display.fill(0)
      txt = [""]
      for line in message.split("\n"):
          for word in line.split(" "):
              next_len = len(txt[-1]) + len(word) + 1
              if next_len*display.textWidth + (next_len-1) > display.width:
                  txt += [""]
              txt[-1] += (" " if txt[-1] else "") + word
          txt += [""]
      for ln, line in enumerate(txt):
          display.drawText(line, 0, (display.textHeight+1)*ln, 1)
      display.display.show()



Title = Sprite(72,24,bytearray([255,255,255,255,255,1,1,237,237,237,255,1,1,231,159,1,1,255,1,1,253,253,1,3,255,1,1,255,255,1,1,255,1,1,221,157,1,99,255,63,7,129,185,129,7,63,255,1,1,231,159,1,1,255,135,3,121,253,253,121,123,255,1,1,237,237,237,255,255,255,255,255,
           255,255,255,255,127,62,158,78,174,86,39,22,134,71,171,82,170,83,42,146,202,114,14,7,39,39,38,134,198,254,255,63,30,206,231,7,31,254,254,126,30,143,231,231,230,198,207,254,126,15,7,38,38,39,167,247,126,14,6,38,39,39,134,198,254,254,254,255,255,255,255,255,
           255,255,231,225,234,229,234,229,242,241,248,248,250,121,26,193,226,249,222,207,203,200,204,207,207,204,200,203,203,201,204,204,204,204,204,200,200,207,207,204,200,201,201,201,204,206,207,203,200,200,201,201,201,205,207,203,200,204,207,207,204,232,251,255,255,255,255,255,255,255,255,255]), Title.x,Title.y,Title.key,Title.mirrorX,Title.mirrorY)
Player = Sprite(15,10,bytearray([183,1,252,0,206,206,205,181,181,204,180,180,0,123,135,
           3,2,0,0,1,1,2,2,2,0,0,0,0,3,3]), Player.x,Player.y,Player.key,Player.mirrorX,Player.mirrorY)
Enemy = Sprite(15,10,bytearray([191,3,252,204,252,204,123,123,123,132,180,204,252,123,135,
           3,3,0,0,0,0,3,3,3,0,0,0,0,3,3]), Enemy.x,Enemy.y,Enemy.key,Enemy.mirrorX,Enemy.mirrorY)
Enemy2 = Sprite(15,10,bytearray([183,3,252,180,132,180,75,123,123,132,180,204,252,51,207,
           3,3,0,0,0,0,3,3,3,0,0,0,0,3,3]), Enemy2.x,Enemy2.y,Enemy2.key,Enemy2.mirrorX,Enemy2.mirrorY)
ScoreName = Sprite(5,21,bytearray([136,235,232,238,136,
           168,170,202,170,136,
           24,14,28,14,24]), ScoreName.x,ScoreName.y,ScoreName.key,ScoreName.mirrorX,ScoreName.mirrorY)
GetReady = Sprite(20,40,bytearray([0,0,255,156,156,201,193,153,57,51,131,255,255,255,255,255,255,255,255,255,
           0,0,255,32,60,121,121,193,249,243,131,255,193,156,156,140,252,252,57,131,
           0,0,255,39,38,96,102,100,100,241,241,255,129,249,243,243,3,243,231,7,
           0,0,255,120,115,230,230,102,102,100,48,255,231,231,207,207,207,207,159,2,
           224,192,255,206,206,252,220,152,146,50,39,255,255,255,255,255,255,255,255,254]), GetReady.x,GetReady.y,GetReady.key,GetReady.mirrorX,GetReady.mirrorY)
sprDigits = Sprite(50//10,3,bytearray([0,2,2,2,0,0,5,5,4,5,0,6,5,3,0,0,3,1,3,0,3,3,0,2,2,0,3,0,6,0,0,2,0,6,0,5,5,5,3,0,0,2,0,2,0,0,3,0,2,0]), sprDigits.x,sprDigits.y,sprDigits.key,sprDigits.mirrorX,sprDigits.mirrorY)
sprDigits.key = 1
display.setFont("/lib/font8x8.bin", 8, 8, display.textSpaceWidth)
Title.x = 0
Title.y = 0
Player.x = 2
Player.y = 15
Enemy.x = -21
Enemy2.x = -21
ScoreName.x = 66
ScoreName.y = 3
display.setFPS(30)
while True:
  while True:
    display.fill(1)
    display.drawSprite(Title)
    display.drawText(str('Press A'), 5, 28, 0)
    Time = 20000
    Score = 0
    if buttons.buttonA.justPressed():
      break
    display.display.show()
  display.fill(1)
  GetReady.x = 30
  GetReady.y = 0
  display.drawSprite(GetReady)
  display.display.show()
  time.sleep(1)
  while True:
    display.setFPS(30)
    display.fill(1)
    display.drawRectangle(-1, 0, 66, 40, 0)
    display.drawLine(0, 13, 63, 13, 0)
    display.drawLine(0, 26, 63, 26, 0)
    display.drawRectangle(5, 13, 9, 14, 1)
    display.drawRectangle(25, 13, 9, 14, 1)
    display.drawRectangle(46, 13, 9, 14, 1)
    display.drawSprite(ScoreName)
    display.drawSprite(Player)
    if Player.y >= 15:
      if buttons.buttonU.justPressed():
        Player.y += -13
    if Player.y <= 15:
      if buttons.buttonD.justPressed():
        Player.y += 13
    if Enemy.x < -20:
      Enemy.x = 50
      i = random.randint(1, 3)
      if i == 1:
        Enemy.y = 2
      elif i == 2:
        Enemy.y = 15
      elif i == 3:
        Enemy.y = 28
    if Enemy2.x < -20:
      Enemy2.x = 50
      r = random.randint(1, 3)
      if r == 1:
        Enemy2.y = 2
      elif r == 2:
        Enemy2.y = 15
      elif r == 3:
        Enemy2.y = 28
    time.sleep_us(Time)
    display.drawSprite(Enemy)
    Enemy.x += -1
    display.drawSprite(Enemy2)
    Enemy2.x += -1
    if Player.x == Enemy.x - 15:
      if Player.y == Enemy.y:
        display.setFont("/lib/font8x8.bin", 8, 8, display.textSpaceWidth)
        __print_to_display__('CRASH!')
        time.sleep(2)
        __print_to_display__(Score)
        time.sleep(3)
        Enemy.x = -21
        Enemy2.x = -21
        break
    if Player.x == Enemy2.x - 15:
      if Player.y == Enemy2.y:
        __print_to_display__('CRASH!')
        time.sleep(2)
        __print_to_display__(Score)
        time.sleep(3)
        Enemy.x = -21
        Enemy2.x = -21
        Score = 0
        Time = 20000
        break
    if Enemy.x == 1:
      Score = (Score if isinstance(Score, Number) else 0) + 1
      Time = (Time if isinstance(Time, Number) else 0) + -250
    num = Score
    sprDigits.x = 66
    sprDigits.y = 33
    for count in range(3):
      sprDigits.setFrame(num % 10)
      num = int(num / 10)
      display.drawSprite(sprDigits)
      sprDigits.y += -4
      display.display.show()

123

#### !!!! BLOCKLY EXPORT !!!! ####