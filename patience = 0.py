patience = 0
dead = False
print("This is a game of choices...")
print(f"every action you take changes the outcome so choose wisely")
start=input(f"Do you wish to start? y/n")
if start.lower() == "y":
    Name=input("What's your name bro...")
    print("Welcome", Name, "... You might think this is an investigation but it's not")
    print(f"It really isn't don't look at me like that")
    print("we just want to chat... ask you a few question and you'll be on your way")
    okay1 = input("is that clear? y/n")
    print("doesn't really matter shut up")
    print("now what were you doing in the scene of the crime.")
    ans1 = input("1- i was taking a stroll 2- what scene what crime who 3- dont say anything 4-I was in the bank but i wasn't with the gang")
    if ans1 == "1":
        print("WHAT?!?! DO YOU THINK I AM STUPID OR SOMETING... sheriff patience -1")
        patience -= 1
    elif ans1 == "2":
        print("DONT PLAY DUMB I KNEW YOU WERE THERE YOU SCUM... sheriff patience -1")
        patience -=1

    elif ans1 == "3":
        print("what you gone deaf?")

    elif ans1== '4':
        print("Now we're talking... what were you doing then in a bank at one am at night?... sheriff patience +1")
        print("1-I was getting money to buy some groceries 2-I was just walking by 3- peanut peanut jelly sandwich")
else:
    print("the sherif pulls his gun out and shoots you. the end")
print("okay thats enough... you've brought this unto yourslef.   He walks out and after a few minutes the zlorp walks in")
zlorp1=("zlorp says WHY WHERE YOU AT THE MALL  zlorpily 1- i wasn't at the mall it was the bank 2- i was buying new clothers 3- zlorp gezeeb moondel barrt")
if zlorp1 == '1':
    print("Didn't you say you wera at the bank? zlorp thinks you're guilty... patience -1")
    patience -=1
elif zlorp1 == '2':
    print("aha a confession! zlorp thinks youre guilty... patience -1")
    patience -1
elif zlorp1=='3':
    print("zleep baboo dawfoom!! you seem to have cursed the zlorp he takes out his gun and shoota you")
    dead = True
if dead == False:
    zlorp2 = input("youre getting really tired you want to make a run for it... do you 1-jump out the window 2- stay for longer and wait 3-you tell him the truth")
    if zlorp2 == '1':
        car=input("you got up and threw your body and flew at the window... while falling you can either fall onto 1-a poor man's car 2- a rich man's car")
        if car == '1':
            print("you died")
        else:
            print("You fall on the rich man's car either way... the cushions on the roof save your life. YOU ESCAPED")
    elif zlorp2 == '2':
        print("zlorp himself grows impatient")
        if patience > 0:
            print("since his patience is", {patience}, "He lets you go... YOU ESCAPED")
        else:
            print("Zlorp isn't patient enough and he shoots you... you die")
    elif zlorp2 == '3':
        print("wooo I see... So you did rob the bank!! Where Did you PUT thE MoneY!?!?!?")
        lie = input("tell the 1-truth 2-lie")
        if lie == '1':
            print("zlorp finds the money and lets you")
        elif lie == '2':
            print("zlorp checks and finds nothing...")
            lie2 = ("this is your last chance human!! 1-lie 2-truth")
            if lie2 == '1':
                print("Zlorp shoots you")
            elif lie == '2':
                print("zlorp finds the money but now you go to jail... bloops")



