def gradepointCalculator():
    numberOfCourses = int(input("Please Enter the number of Courses you Offered: "))
    m = int(input("Enter the total credits of the semester:"))
    print("The total number of credits in the semester:",m)
    print ("***************************************************************************")
    for x in range(numberOfCourses):
        Course1 = input("Enter The Course code of the  course you took:") 
        n = int(input ("How many credits is the Course you took: "))
        score = int(input("Please Enter your Score:"))
        if 90 <= score <= 100:
                    print('Grade recieved is S')
        elif 80 <= score <= 89:
                    print('Grade recieved is A')
        elif 70 <= score <= 79:
                    print('Grade recieved is B')
        elif 60 <= score <= 69:
                    print('Grade recieved is C')
        elif 50 <= score <= 59:
                    print('Grade recieved is D')
        elif 40 <= score <= 49:
                    print('Grade recieved is E')
        else:
                    print('Grade recieved is F')
        if 90 <= score <= 100:
                    total_credits = 10*n
                    print('Total credits earned for the course :', total_credits)
        elif 80 <= score <= 89:
                    total_credits = 9*n
                    print('Total credits earned for the course :', total_credits)
        elif 70 <= score <= 79:
                    total_credits = 8*n
                    print('Total credits earned for the course :', total_credits)
        elif 60 <= score <= 69:
                    total_credits = 7*n
                    print('Total credits earned for the course :', total_credits)
        elif 50 <= score <= 59:
                    total_credits = 6*n
                    print('Total credits earned for the course :', total_credits)
        elif 40 <= score <= 49:
                    total_credits = 5*n
                    print('Total credits earned for the course :', total_credits)
        else:
                    print('Grade recieved is F so 0 credits earned')
              
        print ("********************************************************************")
        
        
gradepointCalculator()

