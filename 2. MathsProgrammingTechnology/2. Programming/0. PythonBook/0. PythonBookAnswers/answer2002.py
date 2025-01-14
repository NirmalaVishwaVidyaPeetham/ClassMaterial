from datetime import date
from random import random

class Course:
    def __init__( self, name, number ):
        self.name = name
        self.number = number
    def __repr__( self ):
        return "{}: {}".format( self.number, self.name )

class Student:
    def __init__( self, lastname, firstname, birthdate, anr ):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.anr = anr
        self.courses = []
    def __str__( self ):
        return self.firstname+" "+self.lastname
    def age( self ):
        today = date.today()
        years = today.year - self.birthdate.year
        if today.month < self.birthdate.month or \
            (today.month == self.birthdate.month \
            and today.day < self.birthdate.day):
            years -= 1
        return years
    def enroll( self, course ):
        if course not in self.courses:
            self.courses.append( course )
    
students = [ 
    Student( "Arkansas", "Adrian", date( 1989, 10, 3 ), 453211 ),
    Student( "Bonzo", "Beatrice", date( 1991, 12, 29 ), 476239 ),
    Student( "Continuum", "Carola", date( 1992, 3, 7 ), 784322 ),
    Student( "Doofus", "Dunce", date( 1993, 7, 11 ), 995544 ) ]
courses =[
    Course( "Vinology", 787656 ),
    Course( "Advanced spoon-bending", 651121 ),
    Course( "Research Skills: Babbling", 433231 )]

for student in students:
    for course in courses:
        if random() > 0.3:
            student.enroll( course )

for student in students:
    print( "{}: {} {} ({})".format( student.anr, 
        student.firstname, student.lastname, student.age() ) )
    if len( student.courses ) == 0:
        print( "\tNo courses" )
    for course in student.courses:
        print( "\t{}".format( course ) )