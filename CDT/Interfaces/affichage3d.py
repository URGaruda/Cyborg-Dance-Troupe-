from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from math import pi, sin, cos 
from panda3d.core import Vec4, Vec3 


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.environment = self.loader.loadModel("models/moonsurface")
        self.environment.reparentTo(self.render)
        
        # Apply scale and position transforms on the model.
        self.environment.setScale(55,55,156)
        self.environment.setPos(-7, 22, 0)

        
        
        self.mode()
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.camera.setPos(10, 10, 96)
        self.camera.setP(90)

        self.useTrackball()
        self.useDrive()

    def mode(self):
        self.ttf= self.loader.loadModel("models/Groundroamer")
        self.environment.setScale(0.0025,0.0025,0.0025)
        self.environment.setPos(44.25,0.25, 10)
        self.ttf.reparentTo(self.render)
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    def move(self):
        self.ttf.setPos(Vec3(44,44,0))

game = Game()
game.run()