import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
p = mc.player.getTilePos()
mc.setBlock(p.x, p.y, p.z, block.SNOW)
while True:
    while True:
        p = mc.player.getTilePos()
        mc.setBlock(p.x, p.y, p.z, block.SNOW)
while True:
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.ICE)
