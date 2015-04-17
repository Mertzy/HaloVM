# 
# File: HaloPlayer.py
# Author: Isaac J. Mertzenich
# (c) 2015
# Created: April 16, 2015
#
# Description: This class creates an instance of a player in a game of Halo. 
#This class inheirits from HaloObject.py in order to function.

#IMPORTS

from HaloObject import HaloObject


class HaloPlayer(HaloObject):

	def __init__(self, emblem, playerName, playerScore, life, shield, primaryWeapon, secondaryWeapon, grenades, specialWeapon, objName, authorization, status, canRespawn, canDespawn, respawnTime, objSize, destructable):

		self.emblem = emblem					#this contains the player info. Most games have some sort of emblem or logo for each individual player that is customizable.
		self.playerName = playerName	   		#holds the name of the player. In the case of Halo, this would be the players GamerTag
		self.objName = objName		       		#holds the HaloObject's name
		self.life = life				   		#total life of a player
		self.shield = shield			   		#total shield strength of the player
		self.primaryWeapon = primaryWeapon		#sets the players primary weapon
		self.secondaryWeapon = secondaryWeapon  #sets the players secondary weapon
		self.grenades = grenades				#sets the players grenades
		self.specialWeapon = specialWeapon		#sets the players specialWeapon
		self.authorization = authorization 		#controls whether or not an item can be altered or not. This is useful for when you need to prevent changes to an object mid game. If True then the item can be changed. False otherwise.
		self.status = status               		#controls whether or not an item is being acted apon (ie Equiped, bumped, moved, etc)
		self.canRespawn = canRespawn	   		#controls whether or not an item can respawn
		self.canDespawn = canDespawn	   		#controls whether or not an item can despawn after respawn time runs down
		self.respawnTime = respawnTime     		#an objects respawn time.  This is a static attribute.
		self.objSize = objSize             		#sets the objects physical size
		self.destructable = destructable   		#controls whether or not a HaloObject can be physically destroyed.
		self.playerScore = playerScore

