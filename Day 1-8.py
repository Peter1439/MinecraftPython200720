# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:54:46 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,137)
mc.setBlock(x-1,y,z,137)
mc.setBlock(x,y,z+1,137)
mc.setBlock(x,y,z-1,137)
mc.setBlock(x+1,y,z+1,137)
mc.setBlock(x-1,y,z+1,137)
mc.setBlock(x+1,y,z-1,137)
mc.setBlock(x-1,y,z-1,137)