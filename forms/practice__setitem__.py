# useful but not used often enough. eyeing for opportunitues


#================================================================================
# Tony Suffolk's stackoverflow example
# https://stackoverflow.com/questions/43627405/understanding-getitem-method
#================================================================================
class Building(object):
    def __init__(self, floors):
        self._floors = [None]*floors
    def occupy(self, floor_number, data):
        self._floors[floor_number] = data
    def get_floor_data(self, floor_number):
        return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1.occupy(0, 'Reception')
building1.occupy(1, 'ABC Corp')
building1.occupy(2, 'DEF Inc')
print( building1.get_floor_data(2) )



class Building(object):
    def __init__(self, floors):
        self._floors = [None]*floors
    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data
    def __getitem__(self, floor_number):
        return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print( building1[2] )
#================================================================================
#================================================================================


# if it were to be used in the siggen function, in this format:
class Siggen():
    def __init__(self):
        self.crit = {
            'dcform' : [10,20,10,20,10],  'SNR' : 30, 
            'physStreng':0.9, 'targetmax' : 0.004, 
            'rdPeak' : 5, 'peakShift' : True
        }
        self.runfunc()
    def __getitem__(self, var):
        try:
            return self.crit[var]
        except:
            print('wrong variable name')

    def __setitem__(self, var, val):
        self.crit[var] = val
        self. runfunc()
    
    def runfunc(self):
        fr = 3.138
        # ...rest of the func...

t = Siggen() # init with default format
t['physStreng'] = 0.3 # rerun with the new variable when reassigning 
t.hbo_mod
