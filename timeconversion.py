def timeConversion(s):
    # print(s[-2:]) PM
    # print(s[:2]) 07
    # print(s[:-2]) 07:05:45
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]