import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

mc = Minecraft.Minecraft.create()

entityIds = mc.getPlayerEntityIds()
EntityId = entityIds[0]

direction = mc.entity.getPitch(EntityId)


mc.postToChat(direction)