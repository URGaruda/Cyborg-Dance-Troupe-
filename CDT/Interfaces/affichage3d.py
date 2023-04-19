from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from math import pi, sin, cos 
from panda3d.core import Vec4, Vec3 
import direct.showbase.ShowBaseGlobal

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.environment = self.loader.loadModel("models/moonsurface")
        self.environment.reparentTo(self.render)
        
        # Apply scale and position transforms on the model.
        self.environment.setScale(200,200,156)
        self.environment.setPos(-7, 22, 0)

        
        
        self.mode()
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.camera.setPos(10, 10, 96)
        self.camera.setP(90)

        self.useTrackball()
        self.useDrive()
        self.taskMgr.add(self.move,"moverobot")

    def mode(self):
        self.ttf= self.loader.loadModel("models/Groundroamer")
        self.environment.setScale(0.0025,0.0025,0.0025)
        self.ttf.setPos(0,0,0)
        self.ttf.reparentTo(self.render)
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        self.camera.disableMouse()
        return Task.cont
    def move(self,task):
        dt= direct.showbase.ShowBaseGlobal.globalClock.getDt()
        self.ttf.setPos(self.ttf.getPos()+Vec3(0.5,0.5,0)*dt)
        print("time=",dt)
        print(self.ttf.getPos())
        return Task.cont
        

game = Game()
game.run()
