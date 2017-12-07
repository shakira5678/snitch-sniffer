elif blockHit.id == block.WOOL.id:
  if blockHit.data == TEAMCOLS[otherTeam]:
        mc.setBlock(x, y, z, block.GLASS.id)
        pointsScored[otherTeam] -= 1
    return pointsScored
players = mc.getPlayerEntityId()
