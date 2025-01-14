class Person:
    def __init__( self, firstname, lastname, age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__( self ):
        return "{} {}".format( self.firstname, self.lastname )
    def underage( self ):
        return self.age < 18

class Student( Person ):
    pass

albert = Student( "Albert", "Applebaum", 19 )
print( albert )
print( albert.underage() )