# ask the candidate the first question
activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n" )

if activity == 'A':
    print("Nice Choice!")
elif activity == 'B':
    print ("Thats great!")
else:
    print ("You must type in A or B, let's just say you like to read.")
    activity = 'A'

# ask the candidate the second question
job = input ("What is your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n")

if job == 'A':
    print("Curator, Nice choice!")
elif job == 'B':
    print("Running a Business? Sounds fun")
else:
    print("You must type in A or B, let's just say you want to be a curator at Smithsonian")
    job = 'A'

# ask the candidate the third question
value = input("What is more important?\n(A) Money\n(B) Love\n")

if value == 'A':
    print("Money, Nice choice!")
elif value == 'B':
    print("Love?, Sounds fun")
else:
    print("You must type in A or B, lets just say money is more important to you")
    value = 'A'


# ask the candidate a fourth question
decade = input( "What's your favorite decade?\n(A) 1910s\n(B) 1980s\n" )
if decade == "A":
    print( "1910s, Nice choice!" )
elif decade =="B":
    print( "1980s? Sounds fun!" )
else:
    print("You must type A or B, let's just say the 1910s is your favorite decade.")
    decade = "A"

# ask the candidate a fifth question
travel = input( "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n" )
if travel == "A":
    print( "Driving, Nice choice!" )
elif travel =="B":
    print( "Flying? Sound fun!" )
else:
    print("You must type A or B, let's just say your favorite way to travel is by driving")
    travel = "A"

# print out their choices
print( f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")


# Variables for scoring
diana_like = 0
steve_like = 0
max_like = 0
barbara_like = 0

# Update variables based on choices

# update scoring variables based on the activity choice
if activity = 'A':
    diana_like = diana_like + 1
    barbara_like = barbara_like + 1
else:
    max_like = max_like + 1
    steve_like = steve_like + 1

# update scoring variables based on the job choice
if job = 'A':
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
    steve_like = steve_like - 1
else:
    max_like = max_like + 2

# update scoring variables based on the value choice
if value = 'A':
    diana_like = diana_like - 1
    max_like = max_like + 2
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 2
    barbara_like = barbara_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    steve_like = steve_like + 2
    diana_like = diana_like + 1
else:
    max_like = max_like + 1
    barbara_like = barbara_like + 2

# update scoring variables based on the travel choice
if travel == "A":
    max_like = max_like + 2
    barbara_like = barbara_like - 1
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 1

# print the results depending on the score
if diana_like >= 6:
    print( "You're most like Wonder Woman!" )
elif steve_like >= 6:
    print( "You're most like Steve Trevor!" )
elif barbara_like >= 6:
    print( "You're most like Barbara Minerva!")
else:
    print( "You're most like Max Lord!")