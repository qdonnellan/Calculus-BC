import re
import random

all_students = '''
Bryan	#
Ethan	#
Jeffrey	#
Bryce	#
Shahrukh	#
Emmanual	#
William	#
Kendyl	#
Hien	#
Jessica	#
Matthew	#
Michael	#
Alessa	#
Holly	#
Tory	#
Jennifer	#
Gilberto	#
Pooja	#
Shawn	#
Philip	#
Vivian	#
Jonah	#
Brendan	#
India	#
Paul	#
Tony	#
Tahsin	#
Amreek	#
Alexis	#
Khoa	#
Stephanie	#
Evangelina	#
Long	#
Laureon	#
Colton
'''
all_students = re.sub('\n', '', all_students) 
all_students = re.sub('\t', '', all_students) 
all_students = all_students.split('#') 
random.shuffle(all_students) 
print "Your randomized groups for the day are: \n"
group1 = ''
group2 = ''
group3 = ''
group4 = ''
for student in all_students[0:9]:
    group1 += student.strip() + ", "
for student in all_students[9:18]:
    group2 += student.strip() + ", "
for student in all_students[18:27]:
    group3 += student.strip() + ", "
for student in all_students[27:]:
    group4 += student.strip() + ", "
    
print "Group 1"
print group1, "\n"
print "Group 2"
print group2, "\n"
print "Group 3"
print group3, "\n"
print "Group 4"
print group4, "\n"


