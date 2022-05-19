# Basic File handeling : Student information

import csv

# Function to store the student information entered by the user in the csv / excel file

def enter_csv(info_list):		
    with open('Student_info.csv','a',newline = '') as csv_file: # here Student_info.csv is the excel filename with .csv extension with 
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Phone No.","E-Mail ID"])
        writer.writerow(info_list)
       

if __name__ == '__main__':
    condition = True
    student_no = 1		# To tell the user the No. of Students information he / she has stored in the file
    
    print("\n Enter Student Information : Name , Age , Phone No. , E-Mail ID\n " + "-" * 62)
    while(condition):
        student_info = input("\n Student No. : {} \t   ".format(student_no))
        
# Splits the student information string by recognizing a space(" ") between the data 
        info_list = student_info.split(' ')		
        
        print("-" * 62+"\n The entered information is : \n Name : {}   Age : {}   Phone No. : {}   E-Mail ID : {}".format(info_list[0],info_list[1],info_list[2],info_list[3]))
        
# Outer condition asks the user if the entered information is correct or not
        info_check = input("\n Is the entered information correct yes / no : ")
        if info_check == "yes":
            enter_csv(info_list)
            print("\n Student {} infromation saved successfully !".format(student_no))
            
# inner contion loop asks user if he / she wants to add information for more students 
            condition_check = input("\n\n Do you want to enter information for another student yes / no ? : ")
            if condition_check == "yes":
                condition = True
                student_no = student_no + 1
            elif condition_check == "no":
                print("\n {} Students Information updated in the csv file !! \n".format(student_no))
                condition = False
        elif info_check == "no":
            print("\n Please re-enter information correctly !\n")
