import re
import random

all_students = '''
Faiyaz#
Elizabeth#
Luke #
Randy	#
Stanley #
Peter	#
Preston #
Gustavo #
Victor #
Nicholas #
Hao #
Jacob #
Michael K.	#
Raymond #
Justin #
Henry 	#
Quan #
Thaichan	#
Thuc #
Michael P.	#
Loana	#
Kylee 	#
Camila #
Farhan	#
Jeremiah #
Rachel	#
Sarankan	#
Teleri 	#
Lance #
Joseph 	#
Lilly	#
Uyen	#
Kimmy	#
Austin 
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



