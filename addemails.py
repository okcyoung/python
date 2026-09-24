def emails(filename):
    with open(filename,"r")as fileR,open("email_addresses.txt","w")as fileW:
        for line in fileR:
            line=line.strip()
            linesplit=line.split(',')
            student_id=linesplit[0]
            first_name=linesplit[1]
            last_name=linesplit[2]
            
            email_address=first_name.lower()+"."+last_name.lower()+"_"+student_id[-4:]+"@student.uwa.edu.au "
#             print(f"for student {first_name}, they have been assigned email address of {email_address}")
#             print(f"For student ID {student_id}, the first name is {first_name}, and the last name is {last_name}")
            fileW.write(email_address+"\n")