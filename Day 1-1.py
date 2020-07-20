# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:49:00 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print(mc.player.getPos())