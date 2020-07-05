# Author: Makaliah Dickinson
# Date: 7/5/2020
# Description: The following formula can be used to determine the distance an object falls due to gravity in a specific
#              time period: d = (1/2)gt2 where d is the distance in meters, g is 9.8, and t is the time in seconds that
#              the object has been falling. Write a function named fall_distance that takes the time in seconds as an
#              argument. The function should return the distance in meters that the object has fallen in that time.
def fall_distance(falling_time):
    return 0.5 * 9.8 * falling_time * falling_time


time = float(input("Enter the amount of time for which the object is falling: "))
print("Distance the object has fallen is", fall_distance(time))
