from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep, time
from random import getrandbits

TRAMCOLS = [13,14]

def buildPitch(mc, pos):
    mc.setBlocks(pos.x - 5, pos.y -1, pos.z - 10,
            pos.x + 5, pos.y + 3, pos.z + 10,
            block.GLASS.id)
    mc.setBlocks(pos.x - 4, pos.y, pos.z - 9,
            pos.x + 5, pos.y + 3, pos.z + 9,
            block.AIR.id)
    mc.setBlocks(pos.x, pos.y, pos.z - 7,
            pos.x, pos.y + 3, pos.z - 1,
            block.GLASS.id)
    mc.setBlocks(pos.x, pos.y, pos.z + 1,
            pos.x, pos.y + 3, pos.z + 7,
            block.GLASS.id)
    pos = mc.player.getTilePos()
    buildPitch(mc, pos)
    sleep(3)
    mc.postToChat("Go!")
    
def splatBlock(mc, x, y, z, team):
    pointsScored = [0,0]
    otherTeam = 1 - team
players = mc.getPlayerEntityId()
start = Time()
gameOver = False
while not gameOver:
    blockHits = mc.events.pollBlockHits()
for hit in blockHits:
    team = players.index(hit.entityId) % 2
pointsScored = splatBlock(mc, hit.posx, hit.pos.y, hit.pos.z, team)
points[0] += pointsScored[0]
points[1] += pointsScored[1]
    
    
points = [0,0]

mc = Minecraft.create()
mc.postToChat("Minecraft Splat")

pos = mc.players.getTilePos()

buildPitch(mc, pos)

sleep(3)

mc.postToChat("Go")

players = mc.getPlayersEntityIds()

start = time()

gameOver = False

while not gameOver:

    blockHits = mc.events.pollBlockHits()

    for hits in blockHits:

        team = players.index(hit.entityId) % 2

        pointsScored = splatBlocks(
            mc, hits.pos.x, hit.pos.y, hit.pos.z, team)
points[0] += pointsScored[0]
points[1] += pointsScored[1]

for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            if getrandbits(1) == 1:
                    pointsScored = splatBlock(mc, hits.pos.x + x,
                                        hit.pos.y +y, hit.pos.z, team)
                    points[0] += pointsScored[0]
                    points[1] += pointsScored[1]

            if time() - start > 30:
                 gameOver = True
                 mc.posToChat("Game Over")
                 mc.posToChat("Green Team = " + str(points[0]))
                 mc.posToChat("Red Team = " + str(points[1]))
            if points[0] > points[1]:
                 mc.posToChat("Green Team Wins")
            else:
                mc.posToChat("Red Team wins")
             
        


