# 
# File: HaloObject.py
# Author: Isaac J. Mertzenich
# (c) 2015
# Created: April 16, 2015
#
# Description: This class defines a generic object in the Halo game
#series. All custom objects (i.e. weapons, items, etc) will inherit
#from this file.

#Any method that starts with "display" will return a value (THIS WILL NOT PRINT ANYTHING).
#Any method that starts with "set" will change a value.

#IMPORTS

from timer import *


class HaloObject:

	def __init__(self, objName, authorization, status, canRespawn, canDespawn, respawnTime, objSize, destructable):

		self.objName = objName		       #holds the HaloObject's name
		self.authorization = authorization #controls whether or not an item can be altered or not. This is useful for when you need to prevent changes to an object mid game. If True then the item can be changed. False otherwise.
		self.status = status               #controls whether or not an item is being acted apon (ie Equiped, bumped, moved, etc)
		self.canRespawn = canRespawn	   #controls whether or not an item can respawn
		self.canDespawn = canDespawn	   #controls whether or not an item can despawn after respawn time runs down
		self.respawnTime = respawnTime     #an objects respawn time.  This is a static attribute.
		self.objSize = objSize             #sets the objects physical size
		self.destructable = destructable   #controls whether or not a HaloObject can be physically destroyed.

	def startRespawnTimer(self, timeToStart):

			countdown(self.objName, timeToStart)

	def setRespawnTime(self, timeChange): #This method changes the respawn time.

		while self.authorization == True:

			self.respawnTime = timeChange #Changes the time until respawn

	def displayRespawnTime(self): #displays the respawn time.  This time is the time that is set for the game, not the current time on the clock.

		return self.respawnTime

	def setRespawnStatus(self, respawnChange): #This method changes whether or not a HaloObject can respawn

		while self.authorization == True:

			self.canRespawn = respawnChange

	def displayRespawnStatus(self): #Returns True if the itme can respawn at some point. Returns False if not.

		return self.canRespawn

	def setDespawnStatus(self, despawnChange): #changes whether or not a HaloObject can despawn after a certain
											   #ammount of time of not be interacted with.
		while self.authorization == True:

			self.canDespawn = despawnChange

	def displayDespawnStatus(self):

		return self.canDespawn

	def setStatus(self, statusChange):

		self.status = statusChange

	def displayStatus(self):

		return self.status

	def setAuthorization(self, authorizationChange):

		self.authorization = authorizationChange

	def displayAuthorization(self):

		return self.authorization

	def setObjSize(self, sizeChange):

		while self.authorization == True:

			self.objSize = sizeChange

	def displaySize(self):

		return self.objSize

	def setDestructable(self, destructableChange):

		while self.authorization == True:

			self.destructable = destructableChange

	def displayDestructable(self):

		return self.destructable


