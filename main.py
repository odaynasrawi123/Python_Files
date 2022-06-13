# main.py

# Issa Misherky    318428778
# Oday Nasrawi     211918628

from Managers import User
from Managers import ProgramManager

inpName = input('Enter userName:')            # type: str
inpPass = input('Enter password:')            # type: str

passHash = User.getUserPassHash(inpName)      # type: str

# if user not found exit program
if not passHash:
    print("User does'nt exist")
    exit(0)

# if continues then check if pass is corret
inpPassHash = User.hashPass(inpPass)
if passHash != inpPassHash:
    print("Incorrect password")
    exit(0)

print("Welcome, " + inpName + "!")


# ============================
# ======== user is in ========
# ============================
    

while True:
    print("Please choose an option:")
    print("1. Append file1 text to file2")
    print("2. Delete file")
    print("3. Swap files content")
    print("4. Remove word from file content")
    print("5. Exits")

    optionNum = input("Enter option number:")  # type: str

    # try parsing to integer
    try:
        optionNum = int(optionNum)             # type: int
    except:
        print("Must be a number")

    # check if option exist
    if optionNum >= 1 and optionNum <= 5:
        {
            1: ProgramManager.option1,
            2: ProgramManager.option2,
            3: ProgramManager.option3,
            4: ProgramManager.option4,
            5: (lambda : {
                    print("Thank you for using our file management program"),
                    exit(0)
                })
        }[optionNum]()
    else:
        print("Option doesn't exist")
