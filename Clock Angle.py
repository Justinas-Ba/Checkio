'''
Analog clocks display time with an analog clock face, which consists of a round dial with the numbers 1 through 12, the hours in the day, around the outside. The hours are indicated with an hour hand, which makes two revolutions in a day, while the minutes are indicated by a minute hand, which makes one revolution per hour. In this mission we will use a clock without second hand. The hour hand moves smoothly and the minute hand moves step by step.

You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in degrees. Don't forget that clock has numbers from 1 to 12, so 23 == 11. The time is given as a string with the follow format "HH:MM", where HH is hours and MM is minutes. Hours and minutes are given in two digits format, so "1" will be writen as "01". The result should be given in degrees with precision ±0.1.

For example, on the given image we see "02:30" or "14:30" at the left part and "01:42" or "13:42" at the right part. We need to find the lesser angle.

Input: A time as a string.

Output: The lesser angle as an integer or a float.
'''


def clock_angle(time):
    # Separate hours from minutes
    converted = time.split(':')
    hr, mins = int(converted[0]), int(converted[1])
    # Calculate the relations betweens hours and minutes
    hr_to_mins = (hr%12)*5+(mins*5/60.0)
    # Find delta between minutes and hours and calculate angle
    answer = abs((mins-hr_to_mins)*6)
    # Return the smaller angle
    if answer > 180.0: return abs(round(360-answer, 1))
    return abs(round(answer, 1))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
