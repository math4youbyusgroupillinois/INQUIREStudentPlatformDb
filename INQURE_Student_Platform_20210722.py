#  
#  DB Script Tool
#  Python - 2021-07-22 19:28:17
#  
#  MODEL CLASSES FOR INQURE_Student_Platform DATABASE
#



# Students.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - INQURE_Student_Platform.Students
# 2021-04-19 10:15:50
#
class Students(Object):

    #
    # Constructor
    #
    # Example: 
    # myStudents = Students( val1, val2,.. )
    #
    def __init__(self, _id = None, middleschool = None, highschool = None, adultbasiceducation = None, developmentaleducation = None, associatesdegreecompletion = None, bachelorsdegreecompletion = None, premedicaleducation = None):
        self.___id = _id
        self.__middleschool = middleschool
        self.__highschool = highschool
        self.__adultbasiceducation = adultbasiceducation
        self.__developmentaleducation = developmentaleducation
        self.__associatesdegreecompletion = associatesdegreecompletion
        self.__bachelorsdegreecompletion = bachelorsdegreecompletion
        self.__premedicaleducation = premedicaleducation


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def middleschool(self):
        return self.__middleschool

    @middleschool.setter
    def middleschool(self, middleschool):
        self.__middleschool = middleschool

    @property
    def highschool(self):
        return self.__highschool

    @highschool.setter
    def highschool(self, highschool):
        self.__highschool = highschool

    @property
    def adultbasiceducation(self):
        return self.__adultbasiceducation

    @adultbasiceducation.setter
    def adultbasiceducation(self, adultbasiceducation):
        self.__adultbasiceducation = adultbasiceducation

    @property
    def developmentaleducation(self):
        return self.__developmentaleducation

    @developmentaleducation.setter
    def developmentaleducation(self, developmentaleducation):
        self.__developmentaleducation = developmentaleducation

    @property
    def associatesdegreecompletion(self):
        return self.__associatesdegreecompletion

    @associatesdegreecompletion.setter
    def associatesdegreecompletion(self, associatesdegreecompletion):
        self.__associatesdegreecompletion = associatesdegreecompletion

    @property
    def bachelorsdegreecompletion(self):
        return self.__bachelorsdegreecompletion

    @bachelorsdegreecompletion.setter
    def bachelorsdegreecompletion(self, bachelorsdegreecompletion):
        self.__bachelorsdegreecompletion = bachelorsdegreecompletion

    @property
    def premedicaleducation(self):
        return self.__premedicaleducation

    @premedicaleducation.setter
    def premedicaleducation(self, premedicaleducation):
        self.__premedicaleducation = premedicaleducation



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Schools.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - INQURE_Student_Platform.Schools
# 2021-04-19 10:15:55
#
class Schools(Object):

    #
    # Constructor
    #
    # Example: 
    # mySchools = Schools( val1, val2,.. )
    #
    def __init__(self, _id = None, hahmodelschoolnetwork = None, johnwinstoncookelementary = None):
        self.___id = _id
        self.__hahmodelschoolnetwork = hahmodelschoolnetwork
        self.__johnwinstoncookelementary = johnwinstoncookelementary


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def hahmodelschoolnetwork(self):
        return self.__hahmodelschoolnetwork

    @hahmodelschoolnetwork.setter
    def hahmodelschoolnetwork(self, hahmodelschoolnetwork):
        self.__hahmodelschoolnetwork = hahmodelschoolnetwork

    @property
    def johnwinstoncookelementary(self):
        return self.__johnwinstoncookelementary

    @johnwinstoncookelementary.setter
    def johnwinstoncookelementary(self, johnwinstoncookelementary):
        self.__johnwinstoncookelementary = johnwinstoncookelementary



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Courses.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - INQURE_Student_Platform.Courses
# 2021-04-19 10:16:10
#
class Courses(Object):

    #
    # Constructor
    #
    # Example: 
    # myCourses = Courses( val1, val2,.. )
    #
    def __init__(self, _id = None, mathematics = None, sciences = None):
        self.___id = _id
        self.__mathematics = mathematics
        self.__sciences = sciences


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def mathematics(self):
        return self.__mathematics

    @mathematics.setter
    def mathematics(self, mathematics):
        self.__mathematics = mathematics

    @property
    def sciences(self):
        return self.__sciences

    @sciences.setter
    def sciences(self, sciences):
        self.__sciences = sciences



    #
    # Methods
    #

    def __str__ (self):
        return ""



# Yellowtexbook_Learning_Resource_Center.py -------------------------------------
from datetime import datetime, date

# 
# Python - Model Class - INQURE_Student_Platform.Yellowtexbook_Learning_Resource_Center
# 2021-04-19 10:16:39
#
class Yellowtexbook_Learning_Resource_Center(Object):

    #
    # Constructor
    #
    # Example: 
    # myYellowtexbook_Learning_Resource_Center = Yellowtexbook_Learning_Resource_Center( val1, val2,.. )
    #
    def __init__(self, _id = None, yellowtextbooktutoringservices = None):
        self.___id = _id
        self.__yellowtextbooktutoringservices = yellowtextbooktutoringservices


    #
    # Properties
    #

    @property
    def _id(self):
        return self.___id

    @_id.setter
    def _id(self, _id):
        self.___id = _id

    @property
    def yellowtextbooktutoringservices(self):
        return self.__yellowtextbooktutoringservices

    @yellowtextbooktutoringservices.setter
    def yellowtextbooktutoringservices(self, yellowtextbooktutoringservices):
        self.__yellowtextbooktutoringservices = yellowtextbooktutoringservices



    #
    # Methods
    #

    def __str__ (self):
        return ""