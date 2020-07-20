# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:34:53 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 11.285
y = 14.39
z = 7.28
mc.player.setPos(x,y,z)