from misc import *
import scraper
from scraper import keywords

# Parses the word tokens scraped and creates a dictionary of wages
def get_wages():
    # Create a dictionary
    wagesDict = {}
    isName = True
    name = ""

    # Iterate through and add each name and wage key value pair to the array
    # If last word was a name, then:
    #       - concat the next word if also name
    #       - add this name as key, and the next value converted to currency as the value
    global keywords
    for word in keywords:
        if is_number(word):
            number = word
            if isName:
                # All names should have a comma
                if not valid_name(name, number):
                    name = ""
                    continue
                wagesDict[name] = as_float(number)
                isName = False
                name = ""
            # Ignore the else case, since it's another number after the wage (expenses)
        else:
            isName = True
            name += word

    return wagesDict

# Return true if:
#   - name has a comma and has no asterisk
#   - number has a comma (not a date)
def valid_name(name, number):
    return "," in name and "*" not in name and "," in number

# Get the statistics for the given dictionary of data
def statistics(dict):
    mean = 0
    minName = list(dict)[0]
    maxName = list(dict)[0]

    for name in dict:
        wage = dict[name]
        mean += wage
        # Check if the current wage < dict[minName]
        if wage < dict[minName]:
            minName = name
        # Max
        if wage > dict[maxName]:
            maxName = name

    length = len(dict)
    mean /= length

    print("Number of employees: " + str(length))
    print("Mean: " + as_currency(mean))
    print("Min wage: " + minName + " has wage of " + as_currency(dict[minName]))
    print("Max wage: " + maxName + " has wage of " + as_currency(dict[maxName]))

def main():
    statistics(get_wages())

main()
