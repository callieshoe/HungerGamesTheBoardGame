#player one
class PlayerOne:
  def __init__(self, name, health,current_square):
    self.name = name
    self.health = health
    self.turn = False
    self.current_square = current_square
    self.eliminated = False
  #show player health
  def getPlayerHealth(self):
    return self.health
  #change players health (based on which square player is on)
  def changePlayerHealth(self, health):
    self.health += health
  #return square player is on
  def getcurrent_square(self):
    return self.current_square
  #change players square
  def changecurrent_square(self, currentSquareChange):
    self.current_square += currentSquareChange
  #make player stay on board
  def fixSquare(self):
    if self.current_square > 24:
      self.current_square = 0
      return self.current_square
    else:
      return self.current_square
  #check to see if a player can still play
  def checkElimination(self):
    if self.health <= 0:
      self.eliminated = True
  #get players name
  def getPlayerName(self):
    return self.name

#player two
class PlayerTwo:
  def __init__(self, name, health,current_square):
    self.name = name
    self.health = health
    self.turn = False
    self.current_square = current_square
    self.eliminated = False
  #show player health
  def getPlayerHealth(self):
    return self.health
  #show player's name
  def getPlayerName(self):
    return self.name
  #change players health (based on which square player is on)
  def changePlayerHealth(self, health):
    self.health += health
  #return square player is on
  def getcurrent_square(self):
    return self.current_square
  #change players square
  def changecurrent_square(self, currentSquareChange):
    self.current_square += currentSquareChange
  #make player stay on board
  def fixSquare(self):
    if self.current_square > 24:
      self.current_square = 0
      return self.current_square
    else:
      return self.current_square
  #check to see if a player can still play
  def checkElimination(self):
    if self.health <= 0:
      self.eliminated = True

#player three
class PlayerThree:
  def __init__(self, name, health,current_square):
    self.name = name
    self.health = health
    self.turn = False
    self.current_square = current_square
  #show player health
  def getPlayerHealth(self):
    return self.health
  #show player's name
  def getPlayerName(self):
    return self.name
  #change players health (based on which square player is on)
  def changePlayerHealth(self, health):
    self.health += health
  #return square player is on
  def getcurrent_square(self):
    return self.current_square
  #change players square
  def changecurrent_square(self, currentSquareChange):
    self.current_square += currentSquareChange
  #make player stay on board
  def fixSquare(self):
    if self.current_square > 24:
      self.current_square = 0
      return self.current_square
    else:
      return self.current_square
  #check to see if a player can still play
  def checkElimination(self):
    if self.health <= 0:
      self.eliminated = True
      
