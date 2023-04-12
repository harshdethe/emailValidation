email=input("Enter your Email :")                      #hdethe76@gmail.com or hdethe76.in
k=j=d=0
if len(email)>=6:
    if email[0].isalpha():                             # index number of 0 (first) is always in alpha
        if ("@" in email) and (email.count("@")==1):   # @ in email and only one is present
            if (email[-4]==".")^(email[-3]=="."):      # reverse index [-4] & [-3] and '^' for only one is right
                for i in email:                        # for loop for iteration
                    if i==i.isspace():                 # to check the space
                        k=1
                    elif i.isalpha():                  # to check alphabet is not in upper case
                        if i==i.upper():
                            j=1
                    elif i.isdigit():                  #write as digit
                        continue
                    elif i=="." or i=="_" or i=="@":   # also use . _ @ 
                        continue
                    else:
                        d=1                            # any symbol use 
                if k==1 or j==1 or d==1:
                    print("Wrong email 5")
                else:
                    print("Right email")
            else:
                print("Please write . in mail")
        else:
            print("@ not present in input email")    
    else:
        print("Enter start email from alphabet")
else:
    print("Email should be greater than 6")
