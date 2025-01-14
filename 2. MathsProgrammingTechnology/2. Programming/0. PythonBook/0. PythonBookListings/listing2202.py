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
    def __init__( self, firstname, lastname, age, program ):
        super().__init__( firstname, lastname, age )
        self.courselist = []
        self.program = program
    def underage( self ):
        return self.age < 21
    def enroll( self, course ):
        self.courselist.append( course )

albert = Student( "Albert", "Applebaum", 19, "CSAI" )
print( albert )
print( albert.underage() )
print( albert.program )
albert.enroll( "Methods of Rationality" )
albert.enroll( "Defense Against the Dark Arts" )
print( albert.courselist )