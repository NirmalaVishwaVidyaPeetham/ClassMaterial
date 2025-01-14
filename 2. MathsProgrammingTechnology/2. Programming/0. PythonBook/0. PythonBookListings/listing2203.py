class Vehicle:
    def __init__( self ):
        self.startpoint = []
        self.endpoints = []
        self.verb = ""
        self.name = ""
    def __str__( self ):
        return self.name
    def isStartpoint( self, p ):
        return NotImplemented
    def isEndpoint( self, p ):
        return NotImplemented
    def travel_speed( self, p1, p2 ):
        return NotImplemented
    def travelVerb( self ):
        return NotImplemented