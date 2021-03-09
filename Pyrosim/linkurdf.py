from Pyrosim.originurdf      import ORIGIN_URDF

from Pyrosim.geometryurdf    import GEOMETRY_URDF

from Pyrosim.inertialurdf    import INERTIAL_URDF

from Pyrosim.visualurdf      import VISUAL_URDF

from Pyrosim.collisionurdf   import COLLISION_URDF

from Pyrosim.commonFunctions import Save_Whitespace

class LINK_URDF:

    def __init__(self,name,pos,size):

        self.name = name

        self.depth = 1

        self.origin   = ORIGIN_URDF(pos)

        self.inertial  = INERTIAL_URDF(self.origin)

        self.geometry = GEOMETRY_URDF(size)

        self.visual    = VISUAL_URDF(self.origin , self.geometry)

        self.collision = COLLISION_URDF(self.origin , self.geometry)

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.inertial.Save(f)

        self.visual.Save(f)

        self.collision.Save(f)

        self.Save_End_Tag(f)

# ------------------- Private methods -----------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</link>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<link name="' + self.name + '">\n')
