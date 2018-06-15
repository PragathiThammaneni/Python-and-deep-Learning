# Python program if we have a list of students who are attending class "Python" and another list of students who are attending class "Web Application".Find the list of students who are attending both the classes.
#Also find the list of students who are not common in both the classes.


class_python=['Pragathi','Sridevi','Abhi','Thammaneni']
class_webapplication=['Pragathi','Abhi','Krishna','Ratna']
common=list(set(class_python).intersection(set(class_webapplication)))
print('Common students in both classes')
print(common)
total=list(set(class_python).union(set(class_webapplication)))
unique=list(set(total).difference(set(common)))
print('Not common /Unique students in both classes')
print(unique)