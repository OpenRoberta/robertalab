# Import
import math
from optparse import OptionParser

import time

from naoqi import *

class Hal(object):

    def __init__(self):
        self.NAO_IP = ""
        parser = OptionParser()
        parser.add_option(
            "--pip", help="Parent broker port. The IP address or your robot", dest="pip")
        parser.add_option(
            "--pport", help="Parent broker port. The port NAOqi is listening to", dest="pport", type="int")
        parser.set_defaults(pip=self.NAO_IP, pport=9559)
        (opts, args_) = parser.parse_args()
        pip = opts.pip
        pport = opts.pport
        # parse command line options
        self.myBroker = ALBroker("myBroker", "0.0.0.0",  # Listen to anyone
                                 0,  # find a free port and use it
                                 pip,  # parent broker ip
                                 pport)  # parent broker port

        # Create ALProxy
        self.tts = ALProxy("ALTextToSpeech")
        self.motion = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        self.memory = ALProxy("ALMemory")
        self.tracker = ALProxy("ALTracker")
        self.mark = ALProxy("ALLandMarkDetection")
        self.photo = ALProxy("ALPhotoCapture")
        self.sonar = ALProxy("ALSonar")
        self.sonar.subscribe("myApplication")
        self.led = ALProxy("ALLeds")
        self.video = ALProxy("ALVideoRecorder")
        self.asr = ALProxy("ALSpeechRecognition")
        self.aup = ALProxy("ALAudioPlayer")
        self.fd = ALProxy("ALFaceDetection")
        self.awareness = ALProxy("ALBasicAwareness")

        self.naoMarkInformation = {}

    # MOVEMENT

    def applyPosture(self, pose):
        # posture.goToPosture is used instead of applyPosture as this is a
        # "intelligent" move calculating the path on its own
        if pose == 'Rest':
            self.motion.rest()
        else:
            self.posture.goToPosture(pose, 0.8)

    def stiffness(self, bodypart, status):
        if status == 1:
            self.motion.setStiffnesses(bodypart, 1.0)
        elif status == 2:
            self.motion.setStiffnesses(bodypart, 0)

    def autonomous(self, mode):
        if mode == 1:
            self.awareness.startAwareness()
            self.motion.setBreathEnabled("Body", True)
        elif mode == 2:
            self.awareness.stopAwareness()
            self.motion.setBreathEnabled("Body", False)
            
    def setAutonomousLife(self, state):
        if state == 'ON':
            self.awareness.startAwareness()
            self.motion.setBreathEnabled("Body", True)
        elif state == 'OFF':
            self.awareness.stopAwareness()
            self.motion.setBreathEnabled("Body", False)
        else:
            pass

    def hand(self, handName, mode):
        if mode == 1:
            self.motion.openHand(handName)
        elif mode == 2:
            self.motion.closeHand(handName)

    def moveJoint(self, jointName, degrees, mode):
        rad = math.radians(degrees)
        if mode == 1:
            self.motion.setAngles(jointName, rad, 0.2)
        elif mode == 2:
            self.motion.changeAngles(jointName, rad, 0.2)

    # WALK

    def walk(self, x, y, theta):
        rad = math.radians(theta)
        self.motion.moveTo(x / 100.0, y / 100.0, rad)

    def stop(self):
        self.motion.stopMove()

    def walkAsync(self, xSpeed, ySpeed, zSpeed):
        '''We get speeds in range 0-100, so we need to normalise them to 0-0.3 m/s'''

        maxSpeed = 0.3

        xSpeed = maxSpeed * (xSpeed / 100.0)
        ySpeed = maxSpeed * (ySpeed / 100.0)
        zSpeed = maxSpeed * (zSpeed / 100.0)
        self.motion.move(xSpeed, ySpeed, zSpeed)

    # ANIMATIONS

    def taiChi(self):
        names = list()
        times = list()
        keys = list()

        self.posture.goToPosture("Stand", 1.0)

        names.append("HeadPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 8.95233e-08, -4.76838e-07, 8.89455e-08, 1.04976e-07, 0.331613, 0.314159, 9.19019e-08, -0.331613, 0.139626, -
                     0.0872665, 0.139626, 0.383972, 0.558505, 0.383972, -0.331613, 0.139626, -0.0872665, 0.139626, 0.383972, 0, -0.190258])

        names.append("HeadYaw")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 8.42936e-08, 8.42938e-08, 8.42938e-08, -4.76838e-07, 0.314159, -0.296706, -1.18682, -0.279253, 0.20944,
                     1.5708, 0.20944, 0.139626, 0, -0.139626, 0.279253, -0.20944, -1.5708, -0.20944, -0.139626, 0, -0.00310993])

        names.append("LAnklePitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 43.4, 44.4, 46.2, 50])
        keys.append([1.00403e-07, 0, -0.303687, 0, 0, -0.647517, -0.610865, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -
                     1.0472, -0.872665, -0.741765, 0, 1.00403e-07, 0.523599, 1.00403e-07, -0.555015, -0.654498, -1.0472, 0.033706])

        names.append("LAnkleRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 33.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0.0523599, 0.122173, 0.174533, -0.10472, -0.10472, 0.174533, -0.261799, 0.0628318, 0.1309,
                     0, 0, 0, 0.0872665, 0, -0.240855, -0.55676, -0.424115, -0.349066, 0, -0.349066, -0.312414, 0, -0.05058])

        names.append("LElbowRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
        keys.append([0, -0.698132, -1.0472, 0, 0, -1.65806, -0.959931, -1.48353, -1.01229, -1.01229, 0, -1.01229, -
                     1.01229, -0.890118, -0.855211, -1.11701, -0.855211, -1.25664, -0.855211, -0.855211, -0.994838, -1.4207, -0.38806])

        names.append("LElbowYaw")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
        keys.append([-1.5708, -1.5708, -1.5708, -1.5708, -1.5708, -0.383972, 0, 0, 0, 0, 0, 0, 0, 0.20944,
                     0.191986, -0.418879, -0.418879, -0.0872665, -0.418879, 0.191986, -0.378736, -0.244346, -1.18276])

        names.append("LHand")
        times.append([3, 50])
        keys.append([0, 0.2984])

        names.append("LHipPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 0, -0.349066, 0, 0, -0.698132, -0.610865, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -
                     1.0472, -0.872665, -0.741765, -0.122173, -0.872665, 0, -0.872665, -0.654498, -1.0472, 0.216335])

        names.append("LHipRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 33.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([-0.0523599, -0.122173, -0.174533, 0.10472, 0.10472, -0.174533, 0.174533, 0.420624, 0.528835, 0.610865,
                     0.610865, 0.610865, 0.349066, 0, -0.261799, 0.251327, 0.261799, 0.139626, 0.698132, 0.139626, -0.261799, 0, 0.0414601])

        names.append("LHipYawPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([-0.10821, -0.120428, -0.1309, -0.120428, -0.143117, -0.167552, -
                     0.0994838, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.0680678, 0, -0.194775])

        names.append("LKneePitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 0, 0.698132, -9.9341e-08, -9.9341e-08, 1.39626, 1.22173, 2.0944, 2.0944, 2.0944,
                     2.0944, 2.0944, 2.1101, 1.74533, 1.48353, 0.122173, 1.74533, 0, 1.74533, 1.309, 2.0944, -0.0890141])

        names.append("LShoulderPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([1.5708, 1.91986, 2.0944, 1.5708, 0, 0.366519, 0.349066, 0.191986, -0.802851, -0.174533, -0.296706, -
                     0.174533, 0.523599, 0.471239, 0.331613, -0.471239, 0.0698132, -0.0698132, 0.0698132, 0.331613, 1.69297, 1.52936])

        names.append("LShoulderRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0.174533, 0.349066, 0.174533, 0.174533, 0.174533, 0.698132, 0, 0.0872665, 0.174533,
                     0.401426, 1.15192, 0.401426, 0.401426, 0.174533, 0, 0.401426, 0, 0, 0, 0.20944, 0.942478, 0.107338])

        names.append("LWristYaw")
        times.append([3, 50])
        keys.append([-1.53589, 0.139552])

        names.append("RAnklePitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([1.00403e-07, 0, 0, 0, 0, -0.698132, -0.174533, 0, 0, 1.00403e-07, 0.523599, 1.00403e-07, -
                     0.741765, -0.872665, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, 0.036858])

        names.append("RAnkleRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([-0.0523599, 0.1309, 0.438078, 0.10472, 0.10472, 0.294961, 0.621337, 0.785398, 0.74351, 0.436332, 0,
                     0.349066, 0.261799, 0, -0.174533, -0.174533, -0.0424667, -0.0225556, -0.0130542, -0.00206581, 0, 0.0291878])

        names.append("RElbowRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
        keys.append([0, 0.698132, 1.0472, 2.57424e-07, 0, 1.23918, 1.64061, 0.0698132, 1.11701, 0.855211, 1.25664, 0.855211,
                     0.855211, 0.890118, 1.01229, 1.01229, 1.01229, 0.0349066, 1.01229, 1.01229, 1.13272, 1.36659, 0.395814])

        names.append("RElbowYaw")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 45.4, 46.2, 50])
        keys.append([1.5708, 1.5708, 1.5708, 1.5708, 1.5708, 0.191986, 0.349066, 1.5708, 0.418879, 0.418879,
                     0.0872665, 0.418879, -0.191986, -0.20944, 0, 0, 0, 0, 0, 0, 0.342085, 0.244346, 1.15966])

        names.append("RHand")
        times.append([3, 50])
        keys.append([0, 0.302])

        names.append("RHipPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 0, 0, 0, 0, -0.698132, -0.174533, -0.10472, -0.122173, -0.872665, 0, -0.872665, -
                     0.741765, -0.872665, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, -1.0472, 0.214717])

        names.append("RHipRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0.0523599, -0.122173, -0.438078, -0.10472, -0.10472, -0.349066, -0.785398, -0.541052, -0.139626, -0.139626, -
                     0.698132, -0.139626, 0.261799, 0, -0.349066, -0.539307, -0.610865, -0.610865, -0.610865, -0.532325, 0, -0.021434])

        names.append("RHipYawPitch")
        times.append([3, 5, 7, 9, 11, 13, 50])
        keys.append([-0.10821, -0.120428, -0.1309, -
                     0.120428, -0.143117, -0.167552, -0.194775])

        names.append("RKneePitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([0, 0, 0, 0, 0, 1.39626, 0.349066, 0.122173, 0.122173, 1.74533, 0, 1.74533,
                     1.48353, 1.74533, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, 2.0944, -0.091998])

        names.append("RShoulderPitch")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([1.5708, 1.91986, 2.0944, 1.5708, 0, 0.174533, 0.610865, 1.0472, -0.471239, 0.0698132, -0.0698132,
                     0.0698132, 0.331613, 0.471239, 0.523599, -0.802851, -0.174533, -0.296706, -0.174533, 0.523599, 1.69297, 1.51563])

        names.append("RShoulderRoll")
        times.append([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23.6, 26.2,
                      28.4, 30.4, 32.4, 34.4, 37, 39.6, 42.2, 44.4, 46.2, 50])
        keys.append([-0.174533, -0.174533, -0.349066, -0.174533, -0.174515, -0.0698132, -0.837758, -1.51844, -0.401426,
                     0, 0, 0, 0, -0.174533, -0.401426, -0.174533, -0.401426, -1.15192, -0.401426, -0.558505, -0.942478, -0.099752])

        names.append("RWristYaw")
        times.append([3, 50])
        keys.append([1.53589, 0.164096])

        self.motion.angleInterpolation(names, keys, times, True)

    def wave(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
        keys.append([0.29602, -0.170316, -0.340591, -
                     0.0598679, -0.193327, -0.01078])

        names.append("HeadYaw")
        times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
        keys.append([-0.135034, -0.351328, -0.415757, -
                     0.418823, -0.520068, -0.375872])

        names.append("LElbowRoll")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([-1.37902, -1.29005, -1.18267, -
                     1.24863, -1.3192, -1.18421])

        names.append("LElbowYaw")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([-0.803859, -0.691876, -0.679603, -
                     0.610574, -0.753235, -0.6704])

        names.append("LHand")
        times.append([1.48, 4.52])
        keys.append([0.238207, 0.240025])

        names.append("LShoulderPitch")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([1.11824, 0.928028, 0.9403, 0.862065, 0.897349, 0.842125])

        names.append("LShoulderRoll")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([0.363515, 0.226991, 0.20398,
                     0.217786, 0.248467, 0.226991])

        names.append("LWristYaw")
        times.append([1.48, 4.52])
        keys.append([0.147222, 0.11961])

        names.append("RElbowRoll")
        times.append([0.64, 1.4, 1.68, 2.08, 2.4,
                      2.64, 3.04, 3.32, 3.72, 4.44])
        keys.append([1.38524, 0.242414, 0.349066, 0.934249, 0.680678,
                     0.191986, 0.261799, 0.707216, 1.01927, 1.26559])

        names.append("RElbowYaw")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 3.72, 4.44])
        keys.append([-0.312978, 0.564471, 0.391128,
                     0.348176, 0.381923, 0.977384, 0.826783])

        names.append("RHand")
        times.append([1.4, 3.32, 4.44])
        keys.append([0.853478, 0.854933, 0.425116])

        names.append("RShoulderPitch")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
        keys.append([0.247016, -1.17193, -1.0891, -1.26091, -1.14892, 1.02015])

        names.append("RShoulderRoll")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
        keys.append([-0.242414, -0.954191, -0.460242, -
                     0.960325, -0.328317, -0.250085])

        names.append("RWristYaw")
        times.append([1.4, 3.32, 4.44])
        keys.append([-0.312978, -0.303775, 0.182504])

        self.motion.angleInterpolation(names, keys, times, True)

    def wipeForehead(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
        keys.append([-0.0261199, 0.427944, 0.308291,
                     0.11194, -0.013848, 0.061318])

        names.append("HeadYaw")
        times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
        keys.append([-0.234743, -0.622845, -0.113558, -
                     0.00617796, -0.027654, -0.036858])

        names.append("LElbowRoll")
        times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
        keys.append([-0.866668, -0.868202, -0.822183, -
                     0.992455, -0.966378, -0.990923])

        names.append("LElbowYaw")
        times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
        keys.append([-0.957257, -0.823801, -1.00788, -
                     0.925044, -1.24412, -0.960325])

        names.append("LHand")
        times.append([1.52, 3.12, 3.8, 4.92])
        keys.append([0.132026, 0.132026, 0.132026, 0.132026])

        names.append("LShoulderPitch")
        times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
        keys.append([0.863599, 0.858999, 0.888144, 0.929562, 1.017, 0.977116])

        names.append("LShoulderRoll")
        times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
        keys.append([0.286815, 0.230059, 0.202446,
                     0.406468, 0.360449, 0.31903])

        names.append("LWristYaw")
        times.append([1.52, 3.12, 3.8, 4.92])
        keys.append([0.386526, 0.386526, 0.386526, 0.386526])

        names.append("RElbowRoll")
        times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
        keys.append([1.28093, 1.39752, 1.57239, 1.24105, 1.22571, 0.840674])

        names.append("RElbowYaw")
        times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
        keys.append([-0.128898, -0.285367, -0.15651,
                     0.754686, 1.17193, 0.677985])

        names.append("RHand")
        times.append([1.36, 2.96, 3.64, 4.76])
        keys.append([0.166571, 0.166208, 0.166571, 0.166208])

        names.append("RShoulderPitch")
        times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
        keys.append([0.0767419, -0.59515, -0.866668, -
                     0.613558, 0.584497, 0.882091])

        names.append("RShoulderRoll")
        times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
        keys.append([-0.019984, -0.019984, -0.615176, -
                     0.833004, -0.224006, -0.214801])

        names.append("RWristYaw")
        times.append([1.36, 2.96, 3.64, 4.76])
        keys.append([-0.058334, -0.0521979, -0.067538, -0.038392])

        self.motion.angleInterpolation(names, keys, times, True)

    def blink(self):
        self.led.fadeRGB("FaceLeds", 0xffffff, 1)
        time.sleep(0.5)
        self.led.fadeRGB("FaceLeds", 0x000000, 1)
        time.sleep(0.5)
        self.led.fadeRGB("FaceLeds", 0xffffff, 1)

    def pointLookAt(self, mode, frame, x, y, z, speed):
        speed = min(max(speed, 1.), 100.)
        speed /= 100.
        if mode == "POINT":
            self.tracker.pointAt("Arms", [x, y, z], frame, speed)
        elif mode == "LOOK":
            self.tracker.lookAt([x, y, z], frame, speed, False)

    # SOUNDS

    def setVolume(self, volume):
        self.tts.setVolume(volume / 100.0)

    def getVolume(self):
        return self.tts.getVolume()

    def getLanguage(self):
        return self.tts.getLanguage()

    def setLanguage(self, language):
        self.tts.setLanguage(language)

    def say(self, text, speed = 30, shape = 30):
        #encode string with UTF-8 because the say method can't handle the unicode representation
        textString = str(text)
        textString = u"{}".format(textString)
        textString = textString.decode("unicode-escape").encode("utf-8")

        speed = max(0, min(100, speed))
        shape = max(0, min(100, shape))
        speed = int(speed * 1.5 + 50) # range 50 - 200
        shape = int(shape * 1.5 + 50) # range 50 - 200
        #additional String containing the parameters (usable with all engines)
        #RSPD = speed [50 - 400%]
        #VCT = voice shape [50 - 200%]
        parameterString = "\\RSPD=" + str(math.floor(speed)) + "\\"
        parameterString += "\\VCT=" + str(math.floor(shape)) + "\\"

        #combine strings and add \RST\ to reset control sequences to default
        self.tts.say(parameterString + textString + "\\RST\\")

    def playFile(self, filename):
        self.aup.playFile("/usr/share/naoqi/wav/" + filename + ".wav")

    def dialog(self, phrase, answer):
        vocabulary = [phrase]
        self.asr.setAudioExpression(True)
        self.asr.setVisualExpression(True)
        self.asr.setVocabulary(vocabulary, False)
        self.asr.subscribe("Open_Roberta")
        while(True):
            recognizedWord = self.memory.getData("LastWordRecognized")
            if recognizedWord[1] == phrase:
                self.tts.say(answer)
                self.asr.setAudioExpression(False)
                self.asr.setVisualExpression(False)
                self.asr.unsubscribe("Open_Roberta")
                break

    def recognizeWord(self, vocabulary):
        self.asr.setAudioExpression(True)
        self.asr.setVisualExpression(True)
        self.asr.pause(1)
        self.asr.setVocabulary(vocabulary, False)
        self.asr.pause(0)
        self.asr.subscribe("Open_Roberta")
        while(True):
            recognizedWord = self.memory.getData("LastWordRecognized")
            if recognizedWord[0] in vocabulary:
                time.sleep(1)
                self.asr.setAudioExpression(False)
                self.asr.setVisualExpression(False)
                self.asr.unsubscribe("Open_Roberta")
                return recognizedWord

    # LIGHTS

    def setLeds(self, name, color, intensity):
        self.led.fadeRGB(name, color, 0.1)

    def setIntensity(self, name, intensity):
        self.led.setIntensity(name, intensity / 100.0)

    def ledOff(self, name):
        self.led.off(name)

    def ledReset(self, name):
        self.led.reset(name)

    def randomEyes(self, duration):
        self.led.randomEyes(duration / 1000)

    def rasta(self, duration):
        self.led.rasta(duration / 1000)

    # VISION

    def recordVideo(self, resolution, cameraId, duration, fileName):
        recordFolder = "/home/nao/recordings/cameras/"
        self.video.stopRecording()
        self.video.setFrameRate(10.0)

        # 0 - 160*120  1 - 320*240  2 - 640*480
        self.video.setResolution(resolution)

        # 0 - Top  1 - Bottom
        if cameraId == "Top":
            self.video.setCameraID(0)
        else:
            self.video.setCameraID(1)

        # self.video.setVideoFormat("MJPG")
        self.video.startRecording(recordFolder, fileName)
        time.sleep(duration / 1000)
        self.video.stopRecording()

    def takePicture(self, cameraId, fileName):
        recordFolder = "/home/nao/recordings/cameras/"

        # 0 - 160*120  1 - 320*240  2 - 640*480  3 - 1280*960
        self.photo.setResolution(1)

        # 0 - Top  1 - Bottom
        if cameraId == "Top":
            self.photo.setCameraID(0)
        else:
            self.photo.setCameraID(1)

        self.photo.setPictureFormat("jpg")
        self.photo.takePicture(recordFolder, fileName)

    # SENSORS

    def accelerometer(self, coordinate):
        return self.memory.getData("Device/SubDeviceList/InertialSensor/Accelerometer{}/Sensor/Value".format(coordinate.upper()))
        
    def gyrometer(self, coordinate):
        return self.memory.getData("Device/SubDeviceList/InertialSensor/Gyroscope{}/Sensor/Value".format(coordinate.upper()))

    def ultrasonic(self):
        # Retrieve sonar data from ALMemory (distance in centimeters)
        return self.memory.getData("Device/SubDeviceList/US/Right/Sensor/Value") * 100

    def fsr(self, side):
        return self.memory.getData("{}FootTotalWeight".format(side))


    def touchsensors(self, position, side):
        side = side.title()
        if position == "hand":
            return self.memory.getData("Hand{}BackTouched".format(side)) == 1
        elif position == "bumper":
                return self.memory.getData("{}BumperPressed".format(side)) == 1
        elif position == "head":
            return self.memory.getData("{}TactilTouched".format(side)) == 1
        return False

    def getDetectedMarks(self):
        data = self.memory.getData("LandmarkDetected")
        if (not data is None and len(data) != 0):
            marks = data[1]
        else:
            return [-1]
        result = []
        for mark in marks:
            result.append(mark[1][0])
            self.naoMarkInformation[mark[1][0]] = mark[0][1:] #alpha, beta, xangle, yangle, heading
        return list(result)

    def getDetectedMark(self):
        data = self.memory.getData("LandmarkDetected")
        if (not data is None and len(data) != 0):
            marks = data[1]
        else:
            return -1
        result = marks[0][1][0]
        self.naoMarkInformation[marks[0][1][0]] = marks[0][0][1:] #alpha, beta, xangle, yangle, heading
        return result

    def getElectricCurrent(self, jointName):
        return self.memory.getData("Device/SubDeviceList/" + jointName + "/ElectricCurrent/Sensor/Value")

    def wait(self, timeMilliSeconds):
        timeSeconds = timeMilliSeconds / 1000
        time.sleep(timeSeconds)

    def getNaoMarkInformation(self, id):
        if (id in self.naoMarkInformation):
            return self.naoMarkInformation[id]
        else:
            return [-1]
