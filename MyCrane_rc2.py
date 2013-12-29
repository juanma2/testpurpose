import numpy
global zAxis,MATRIX
zAxis=[]
MATRIX = 10


class Present():
    """  A Simple Present defintion  """
    def __init__(self,myarr):
        self.x, self.y , self.z= myarr[1], myarr[2], myarr[3]
        self.id = myarr[0]

    def turnPresent(self):
        """ You can turn the presents to extend as much base as possible  """
        temp_turn=[self.x, self.y , self.z]
        temp_turn.sort(reverse=True)
        self.x, self.y , self.z =temp_turn[0],temp_turn[1],temp_turn[2]

class Crane(Present):
    """ MY crane will get the Present and will put them where the manager say """
    def __init__(self,Present):
        pass

    def putPresent(self,Present,destxyz,presentlist):
        #deletefrom list()
        print "Crane:"
        #Turn Present to fill as much base as possible
        presentsize=[Present.x,Present.y,Present.z]
        #First put in the sleigh
        self.tellSleighManager(Present,destxyz)
        #them delete it from the presentlist
        presentlist.pop(int(Present.id)-1)
        print "elment id "+str(Present.id)+" is removed!!"
        return True

    def tellSleighManager(self,Present,destxyz):
        ##Our Storage Manager will NOT Change destination or present disposition at all.
        mysleigh =  Sleigh()
        mysleigh.sleighGetLayers(int(Present.z),int(destxyz[2]))
        mysleigh.writePresent(Present,destxyz)
        pass



class Sleigh():
    def __init__(self):
        self.matrixsize = MATRIX
        pass

    def sleighGetLayers(self,numbersoflayers,baselayers):
        print "We have to check "+str(numbersoflayers)+" LAYERS from zAxis level:"+str(baselayers)
        for i in range(numbersoflayers):
            print "checkin layer:"+str(baselayers+i)
            self.existLayer(baselayers+i)
        pass

    def existLayer(self,zlayer):
        #Check in a Array in zXXX exist or create it
        #This is the worst way... but did not found any other one
        try:
            if zAxis[zlayer]:
                print "that layer exist..."
        except:

            #if zAxis[zlayer]:
            #if zlayer not in zAxis:
                zAxis.append(zlayer)
                print "We are createing Layer " + str(zlayer)
                zAxis[zlayer]=[[0 for a in range(self.matrixsize)] for b in range(self.matrixsize)]

        return True

    def writePresent(self,Present,destxyz):
        ##must write id in all elements in matrix
        result = False
        for i in range(int(Present.z)):
            print "In zAxis Layer  " + str(i) + ":"

            for j in range(int(Present.y)):

                for k in range(int(Present.x)):

                    zAxis[i][j][k]=int(Present.id)
                    pass
                    #print "I am writting in "+ str(j) + " , " + str(k) +" position"
    




#### INITIALIZE
##This will load the present list
data = numpy.genfromtxt("/home/adminuser/santa/mini_present",delimiter=",")
mylist=[Present(i) for i in data]
#This Will create a Base Z axis
zAxis = []
#### END INITIALIZE


print "Present size:"
##This will place the "currentitem" from mylist in PosXYZ
currentpresent=mylist[0]
print currentpresent.x
print currentpresent.y
print currentpresent.z
DestPosXYZ=[0,0,0]
currentpresent.turnPresent()
currentjob=Crane(currentpresent)
currentjob.putPresent(currentpresent,DestPosXYZ,mylist)
################

################
currentpresent=mylist[0]
DestPosXYZ=[0,0,0]
currentpresent.turnPresent()
currentjob=Crane(currentpresent)
currentjob.putPresent(currentpresent,DestPosXYZ,mylist)
################
t=0


#print zAxis
#
for i in zAxis:
    print "z"+str(t)+":"
    t=t+1
    for j in i:
        print j
##

#print sleighz0

