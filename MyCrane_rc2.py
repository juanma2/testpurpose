import numpy
global zAxis,MATRIX
zAxis=[]
MATRIX = 20



def printzAxis():
    """ helper function to chow azxis
    """
    t=0
    for i in zAxis:
        print "z"+str(t)+":"
        t=t+1
        for j in i:
            print j



class Present():
    """  A Simple Present defintion  """
    def __init__(self,myarr):
        self.x, self.y , self.z= int(myarr[1]), int(myarr[2]), int(myarr[3])
        self.id = int(myarr[0])

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
        mysleigh =  SleighStorageManager()
        mysleigh.sleighGetLayers(int(Present.z),int(destxyz[2]))
        mysleigh.writePresent(Present,destxyz)
        pass



class SleighStorageManager():
    def __init__(self):
        self.matrixsize = MATRIX
        pass

    def sleighGetLayers(self,numbersoflayers,baselayers):
        """ Will take care of handle current layers if not exist   """
        for i in range(numbersoflayers):
            print "checkin layer:"+str(baselayers+i)
            self.existLayer(baselayers+i)
        pass

    def existLayer(self,zlayer):
        """ @type   zlayer: int
            @param  zlayer: layer number
            @reutrn True if layer exist False if does not exist and create it
        Chack layer availability        """
        #This is the worst way... but did not found any other one
        try:
            if zAxis[zlayer]:
                print "that layer exist..."
                return True
        except:
                zAxis.append(zlayer)
                print "We are createing Layer " + str(zlayer)
                zAxis[zlayer]=[[0 for a in range(self.matrixsize)] for b in range(self.matrixsize)]
                return False

    def fitInLong(self,Present,destxyz):
        print "we are checking if long fits"
        #TODO:Could turn x and y to check it....
        if destxyz[0] + Present.x >MATRIX or destxyz[1] + Present.y >MATRIX:
            print "and we now that not fit"
            return False
        return True

    def fitInPlace(self,Present,destxyz):
        """ @type Present: Present
            @type destxyz: array
            @param destxyz: X Y Z pos
            @return True if Fits
            arraywrite elements id in out sleigh """

        #check if layers exist...
        fitresult=False
        mustchecklayers=False

        if not self.fitInLong(Present,destxyz):
            print "we think that not fit"
            mustchecklayers=False
            fitresult=False
            return False
        else:
            fitresult=True

        for i in range(int(destxyz[2]),Present.z+int(destxyz[2])):
            if self.existLayer(i) is True:
                mustchecklayers=True
                fitresult=True


        print "lets check layers"+ str(mustchecklayers)+" and we think that fit:"+str(fitresult)
        if mustchecklayers is True:
            #I should check before if there is long (X,Y) space enough to fit the present
            ##TODO: look if try except is expensive and remove it
            fitresult=True
            for i in range(int(destxyz[2]),Present.z+int(destxyz[2])):
                print "In zAxis Layer  " + str(i) + ":"

                for j in range(int(destxyz[1]),Present.y + int(destxyz[1])):

                    for k in range(int(destxyz[0]),Present.x + int(destxyz[0])):

                        if zAxis[i][j][k] != 0:
                            #Will never return here... but, why wait? better ideas?
                            print "I am in " + str(i) + " , " + str(j) + " , " + str(k) +" that has value of" + str(zAxis[i][j][k])
                            fitresult = False
                            return False


        return fitresult


    def writePresent(self,Present,destxyz):
        """ write elements id in oput sleigh """
        ##must write id in all elements in matrix
        result = False
        for i in range(destxyz[2],destxyz[2] + Present.z):
            print "In zAxis Layer  " + str(i) + ":"

            for j in range(destxyz[1],destxyz[1] + Present.y):

                for k in range(destxyz[0], destxyz[0] +Present.x):

                    zAxis[i][j][k] = Present.id
                    pass
                    #print "I am writting in "+ str(j) + " , " + str(k) +" position"




#### INITIALIZE
##This will load the present list
data = numpy.genfromtxt("/home/adminuser/santa/mini_present",delimiter=",")
mylist=[Present(i) for i in data]
#This Will create a Base Z axis
zAxis = []
#### END INITIALIZE


##This will place the "currentitem" from mylist in DestPosXYZ
#currentpresent.x  #currentpresent.y #currentpresent.z
mysleigh =  SleighStorageManager()


#################
#Usage:
##Get a present from the list
currentpresent=mylist[0]
##Say where you want to place it
DestPosXYZ=[1,0,0]
##Spin it as you wish
currentpresent.turnPresent()
##check if its Fit there where you wnat...
if SleighStorageManager.fitInPlace(mysleigh , currentpresent,DestPosXYZ) is True:
    ##Tell the Crane that has some job to do
    currentjob=Crane(currentpresent)
    ##Tell the Crane that put in its place
    currentjob.putPresent(currentpresent,DestPosXYZ,mylist)
    ##show my the results
    printzAxis()

