from datetime import date
# Methods for printing out info about Geoff

def getCommands():

    return "Here's everything I can do for you :face_with_cowboy_hat: \n\n" \
           "\t:ye: *gif*: Enter something you'd like to see a gif of :weary:\n" \
           "\t\t\t\t_i.e._ `@geoff gif fire me north`\n\n" \
           "\t:ye: *help*: Ask me a coding question and I'll " \
           "check if I can find an answer on StackOverflow :party_parrot:\n" \
           "\t\t\t\t_i.e_. `@geoff help how do interfaces work?`\n\n" \
           "\t:ye: *rooms*: Enter the date to find when ILC rooms are free :books:" \
           " No inputted date will default to today!\n" \
           "\t\t\t\t_i.e._ `@geoff rooms " + getDate() + "` _[format is DD/MM/YY]_"


def getDate():
       today = date.today()
       return f"{today.day}/{today.month}/" + f"{today.year}"[2:]