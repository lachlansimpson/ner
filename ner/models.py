""" models.py

Has classes for:
    Person : for individuals
    Experience: for an individuals job history
    ShipExperience: for an individual's job history on ships
    Certificate : for an individuals schooling history
    FTCQualification: for an individuals FTC history
    Organisation: for Organisations
    Jobs: for jobs

There are choices defined for: Islands, yes/no, gender(M/F), marital status
(S/M), Industry codes via ILO (ISIC), Occupation codes via ILO (ISOC), and
Salary levels

"""

from django.db import models

ISLAND_CHOICES = (
    ('01',u'Tarawa'),
    ('02',u'Kiritimati'),
    ('03',u'Makin'),
    ('04',u'Butaritari'),
    ('05',u'Marakei'),
    ('06',u'Maiana'),
    ('07',u'Kuria'),
    ('08',u'Aranuka'),
    ('09',u'Abemana'),
    ('10',u'Nonuti'),
    ('11',u'Tabiteua'),
    ('12',u'Onotoa'),
    ('13',u'Beru'),
    ('14',u'Nikunau'),
    ('15',u'Tamana'),
    ('16',u'Arorae'),
    ('17',u'Banaba'),
    ('18',u'Teraina'),
    ('19',u'Kanton'),
    ('20',u'Tabuaeran'),
    ('21',u'Other'),
    ('22',u'N/A'),
    ('23',u'All Islands'),
)

YESNO_CHOICES = (
    (u'Y', u'Yes'),
    (u'N', u'No'),
)    

GENDER_CHOICES = (
    (u'M',u'Male'),
    (u'F',u'Female'),
)

MARRIED_CHOICES = (
    (u'S',u'Single'),
    (u'M',u'Married'),
)

ORG_CAT_CHOICES = (
    ('G',u'Government'),
    ('P',u'Private'),
    ('O',u'Overseas'),
    ('A',u'Agency'),
    ('E',u'Education'),
    ('Z',u'Not Applicable'),
)

SALARY_LEVELS = (
    ('20',u'Level 20'),
    ('19',u'Level 19'),
    ('18',u'Level 18'),
    ('17',u'Level 17'),
    ('16',u'Level 16'),
    ('15',u'Level 15'),
    ('14',u'Level 14'),
    ('13',u'Level 13'),
    ('12',u'Level 12'),
    ('11',u'Level 11'),
    ('10',u'Level 10'),
    ('09',u'Level 9'),
    ('08',u'Level 8'),
    ('07',u'Level 7'),
    ('06',u'Level 6'),
    ('05',u'Level 5'),
    ('04',u'Level 4'),
    ('03',u'Level 3'),
    ('02',u'Level 2'),
    ('01',u'Level 1'),
    ('NA',u'Not Applicable'),
)

ISIC_CODES = (
    ('A',u'Agriculture, forestry and fishing'),
    ('B',u'Mining and quarrying'),
    ('C',u'Manufacturing'),
    ('D',u'Electricity, gas, steam and air conditioning supply'),
    ('E',u'Water supply; sewerage, waste management and remediation activities'),
    ('F',u'Construction'),
    ('G',u'Wholesale and retail trade; repair of motor vehicles and motorcycles'),
    ('H',u'Transportation and storage'),
    ('I',u'Accommodation and food service activities'),
    ('J',u'Information and communication'),
    ('K',u'Financial and insurance activities'),
    ('L',u'Real estate activities'),
    ('M',u'Professional, scientific and technical activities'),
    ('N',u'Administrative and support service activities'),
    ('O',u'Public administration and defence; compulsory social security'),
    ('P',u'Education'),
    ('Q',u'Human health and social work activities'),
    ('R',u'Arts, entertainment and recreation'),
    ('S',u'Other service activities'),
    ('T',u'Activities of households as employers; undifferentiated activities of households for own use'),
    ('U',u'Activities of extraterritorial organizations and bodies'),
)

ISCO_CODES = (
    ('0','Armed forces occupations'),
    ('1','Managers'),
    ('2','Professionals'),
    ('3','Technicians and associate professionals'),
    ('4','Clerical support workers'),
    ('5','Service and sales workers'),
    ('6','Skilled agricultural, forestry and fishery workers'),
    ('7','Craft and related trades workers'),
    ('8','Plant and machine operators, and assemblers'),
    ('9','Elementary occupations'),
)

class Requirement(models.Model):
    class Meta:
        verbose_name = "Job Requirement"
        verbose_name_plural = "Job Requirements"

    req_name = models.CharField("Requirement title",max_length=25)
    req_notes = models.CharField("Requirement note",max_length=100,
                                 blank='True')
    def __unicode__(self):
        """ Requirement reference"""
        if self.req_notes:
            return self.req_name + ', ' + self.req_notes
        else:
            return self.req_name

class Person(models.Model):
    class Meta: 
        verbose_name_plural = "People"

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dob = models.DateField('Date of Birth')  
    gender = models.CharField(max_length='1',choices=GENDER_CHOICES,
                              default='M')
    marital_status = models.CharField(max_length=1,choices=MARRIED_CHOICES,
                                      blank='True',default='S')
    religion = models.CharField(max_length=15,blank='True')
    number_of_dependants = models.IntegerField(blank='True',null='True')

    current_address = models.CharField(max_length=60)
    previous_address = models.CharField(max_length=60, blank='True')

    home_island = models.CharField(max_length=2, choices=ISLAND_CHOICES,
                                   default='01', blank='True')

    birth_place = models.CharField(max_length=2,choices=ISLAND_CHOICES,
                                   default='01', blank='True')

    island_represented = models.CharField(max_length=2, choices=ISLAND_CHOICES,
                                          default='01', blank='True')

    phone_mobile = models.CharField(max_length=12,blank='True')
    phone_home = models.CharField(max_length=8,blank='True')
    phone_other = models.CharField(max_length=12,blank='True')
    email = models.EmailField(blank='True')

    passport_no = models.CharField(max_length=6,blank='True')
    discharge_book = models.CharField(max_length=12,blank='True')

    medical_test_date = models.DateField('Date of last medical test',blank='True',null='True')
    
    skills = models.ManyToManyField(Requirement)

    def __unicode__(self):
        """Person reference: full name and ID # """
        """ return self.first_name + ' ' + self.surname + ', ' + self.pk """
        return self.first_name + ' ' + self.surname

class FTCQualification(models.Model):
    class Meta:
        verbose_name = "FTC Qualification"
        verbose_name_plural = "FTC Qualifications"

    person = models.ForeignKey('Person', blank='True', null='True')    
    cadet_no = models.CharField('Cadet #',max_length=12, blank='True')
    year_grad = models.CharField('Year of graduation',max_length=5, blank='True')

class Certificate(models.Model):
    person = models.ForeignKey('Person', blank='True', null='True')
    institute = models.CharField(max_length=12)
    program = models.CharField(max_length=100)
    course_content = models.CharField(max_length=200)
    duration = models.CharField(max_length=10)

    def __unicode__(self):
        """Certificate reference - program name and institution"""
        return self.program +', ' + self.institute

class Organisation(models.Model):
    name = models.CharField(max_length=50)
    island = models.CharField(max_length=2,choices=ISLAND_CHOICES,blank='True')
    address = models.CharField(max_length=60)
    contact_name = models.CharField(max_length=40,blank='True')
    contact_phone_1 = models.CharField('Phone 1', max_length=9,blank='True')
    contact_phone_2 = models.CharField('Phone 2', max_length=9,blank='True')
    contact_email = models.EmailField('Email')
    industry = models.CharField(max_length=4,choices=ISIC_CODES,blank='True')
    category = models.CharField(max_length=1,choices=ORG_CAT_CHOICES)

    def __unicode__(self):
        """ Organisational reference"""
        if self.island:
            return self.name + ', ' + self.get_island_display()
        else:
            return self.name + ', all islands'

class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = "Vacancies"
    
    title = models.CharField(max_length=50)
    occupation_code = models.CharField(max_length=4,choices=ISCO_CODES)
    organisation = models.ForeignKey('Organisation')
    division = models.CharField("Division within Organisation",max_length=30,
                                blank='True')
    salary_level_1 = models.CharField("Salary minimum under the bar",
                                      max_length=2, choices=SALARY_LEVELS, default='10')
    salary_level_2 = models.CharField("Salary maximum under the bar",
                                      max_length=2, choices=SALARY_LEVELS,
                                      default='10')
    salary_level_3 = models.CharField("Salary minimum over the bar",
                                      max_length=2, choices=SALARY_LEVELS,
                                      default='10')
    salary_level_4 = models.CharField("Salary maximum over the bar",
                                      max_length=2, choices=SALARY_LEVELS,
                                      default='10')

    closing_date = models.DateField()
    requirements = models.ManyToManyField(Requirement)

    def __unicode__(self):
        """ Vacancy reference """
        return self.title + ' at ' + self.organisation.name + ',  ' + str(self.closing_date)

class Experience(models.Model):
    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"

    person = models.ForeignKey('Person')
    title = models.CharField(max_length=40)
    organisation = models.ForeignKey('Organisation')
    start_date = models.DateField()
    end_date = models.DateField()
    reference_name = models.CharField(max_length=30, blank='True', null='True')
    reference_contact_email = models.CharField(max_length=40, blank='True',
                                               null='True')
    reference_contact_phone = models.CharField(max_length=10,
                                               blank='True', null='True')

class ShipExperience(models.Model):
    class Meta:
        verbose_name = "Ship Experience"
        verbose_name_plural = "Ship Experience"

    person = models.ForeignKey('Person',blank='True',null='True')
    recruiting_agency = models.CharField(max_length=12)
    embark_date = models.DateField()
    disembark_date = models.DateField()
    vessel_name = models.CharField(max_length=20)
    vessel_type = models.CharField(max_length=30)
    vessel_company = models.CharField(max_length=10)

    def __unicode__(self):
        """Ship Experience Reference - to and from dates, and the ship name"""
        dates = str(self.embark_date) + ' - ' + str(self.disembark_date) + ', '
        return dates + self.vessel_name
