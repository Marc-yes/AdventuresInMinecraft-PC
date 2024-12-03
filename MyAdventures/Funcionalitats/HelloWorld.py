import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mcpi.minecraft as Minecraft
import mcpi.block as block
 
# Connect to the Minecraft game  
mc = Minecraft.Minecraft.create()       #Del fitxer Minecraft agafem la classe Minecracft

# Interact with the Minecraft world
mc.postToChat("Hello Minecraft World")
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)