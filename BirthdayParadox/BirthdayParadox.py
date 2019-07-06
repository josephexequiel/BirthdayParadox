import random
import prettytable


def same_birthdays(input):
    count = 0
    #Count is going to store the number of times that we have the same birthdays
    timesToRun = 1000
    #timesToRun is going to be sampling size. Higher = More Accurate Result = More Time needed to run as it will need to iterate between a huge sampling size.
    for i in range(0,timesToRun):
        birthdayList = []
        for j in range(0,input):
            random_birthday = random.randint(1,365)
            #Generate a random value between 1 and 365 and make it represent a day in a year.
            birthdayList.append(random_birthday)
            #Add the random value to a list
            birthdayList = sorted(birthdayList)
            #Sort out the list
        for j in range(0, len(birthdayList)-1):
            if (birthdayList[j] == birthdayList[j+1]):
                count+=1;
                probability_same = (count/timesToRun);
                probability_notsame = (1-probability_same);
                percentvar = probability_same*100;
                break 
            #leaving this nested for-loop
    return input, count, probability_notsame, probability_same, percentvar;

def main():
    x = prettytable.PrettyTable(["People (Bit Size)", "Match Found After Sampling #", "Probability No", "Probability Yes", "Birthday Paradox %"]);
    x.add_row(same_birthdays(16));
    x.add_row(same_birthdays(23));
    x.add_row(same_birthdays(32));
    x.add_row(same_birthdays(64));
    x.add_row(same_birthdays(70));
    x.add_row(same_birthdays(128));
    x.add_row(same_birthdays(256));
    x.add_row(same_birthdays(512));
    print(x);

if __name__== "__main__":
    main()