from naoqi import *
import time

class FaceRecognitionModule(ALModule):

    def __init__(self, name):
        ALModule.__init__(self, name)
        self.fd = ALProxy("ALFaceDetection")
        self.memory = ALProxy("ALMemory")
        self.BIND_PYTHON(self.getName(), "onFaceRecognized")
        self.memory.subscribeToEvent("FaceDetected", self.getName(), "onFaceRecognized")
        self.lastFaceRecognized = ""
        self.isFaceRecognized = False
        self.fd.clearDatabase()
        self.naoFaceInformation = {}

    def learnFace(self, name):
        return self.fd.learnFace(name)

    def forgetFace(self, name):
        return self.fd.forgetPerson(name)

    def detectFace(self):
        while(not self.isFaceRecognized):
            time.sleep(0.1)
        self.isFaceRecognized = False
        return self.lastFaceRecognized[0]
    def detectFaces(self):
        while(not self.isFaceRecognized):
            time.sleep(0.1)
        self.isFaceRecognized = False
        return self.lastFaceRecognized

    def getFaceInformation(self, name):
        if (name in self.naoFaceInformation):
            return list(self.naoFaceInformation[name])
        else:
            return list([-1])

    def onFaceRecognized(self, key, value, message):
        data = self.memory.getData("FaceDetected")

        if len(data) == 0:
            self.lastFaceRecognized = [-1]
            self.isFaceRecognized = False
        else:
            faces = data[1][:-1]
            result = []
            for face in faces:
                result.append(face[1][2])
                if not face[1][2] == "":
                    self.naoFaceInformation[face[1][2]] = face[0][1:] #alpha, beta, xangle, yangle, heading
            print result
            self.lastFaceRecognized = list(result)
            self.isFaceRecognized = True

    def unsubscribe(self):
        self.memory.unsubscribeToEvent("FaceDetected", self.getName())
