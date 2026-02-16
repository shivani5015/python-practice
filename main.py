from result_system.report import result
from result_system.marks import total,percentage
from result_system.grade import grade
sub1=int(input("enter marks"))
sub2=int(input("enter marks"))
sub3=int(input("enter marks"))
total_marks,percentage_marks,grade_obtained=result(sub1,sub2,sub3)
print("total marks:",total_marks)
print("percent marks:",percentage_marks)
print("grade obtained:",grade_obtained)




