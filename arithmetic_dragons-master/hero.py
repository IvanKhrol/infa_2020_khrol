# coding: utf-8
# license: GPLv3
from gameunit import *
from enemies import *

class Hero(Attacker):
    def __init__(self,name):
        self._health = 100
        self._attack = 50
        self._name= None
        self._experience = 0

