'''
The bill is represented as an array with information about the calls. Help Nicola to calculate the cost for each of Sophia calls. Each call is represented as a string with date, time and duration of the call in seconds in the follow format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time in this information are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count on the day when they began. For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;
For example:

2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.
Input: Information about calls as a tuple of strings.

Output: The total cost as an integer.
'''


def total_cost(calls):
    import math
    bill = 0
    started = None
    for call in calls:
        call = call.split()
        # Expressing seconds to minutes; Rounding to bigger number
        mins = math.ceil(int(call[2])/60)
        # Store todays date so we can check with later days
        if call[0] == started:
        # We need to check to things:
        # have we talked more than 100 mins today, or not?
            if (history + mins) > 100:
                if history >= 100:
                    bill += mins*2
                if history < 100:
                    bill += (100-history) + (mins-(100-history))*2
            else:
                bill += mins
            history += mins
        # Only check when day is different than previous call
        else:      
            if mins > 100:
                bill += 100 + (mins-100)*2
            else:
                bill += mins
            history = mins
        started = call[0]
    return bill

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
