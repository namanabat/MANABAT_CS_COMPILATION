students [] 

for i in range(3): 
    student_info = {}
    student_info["name"]=input("Enter the name:")
    student_info["age"]=input("Enter the age:")
    student_info["grade"]=input("Enter the grade:")
    students.append(student_info)
    
    for j in students: 
        print ("\n Class Directory") 
        print ("name:", i["name"])
        print ("age:", i["age"])
        print ("grade:", i["grade"])
        
        
        
