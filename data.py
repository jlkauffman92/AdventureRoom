from classes import *
#constants


#scene 1

#items
GLOBE = Item("globe", "You can see the whole world!", [{'spin':'It spins for a while then stops.'}])
CHESSBOARD = Item("chess board", "someone is losing badly")
GUN = Weapon("gun", "it shoots", [{'shoot':'no ammo!'}], 15)

#Scene 1
S1_ITMES = [GLOBE, CHESSBOARD]
S1 = Scene(1, "You find yourself at a small table. There is a globe and a chess board.", S1_ITMES)

SCENES = [S1]