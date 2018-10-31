import time
import stddraw
import datetime
import math

#this clock is based off the unit circle

#x and y values as points on the unit circle
x_value_unit_circle = [0,0.5,(3**(1/2))/2,1,(3**(1/2))/2,0.5,0,-0.5,-(3**(1/2))/2,-1,-(3**(1/2))/2,-0.5]
y_value_unit_circle = [1,(3**(1/2))/2,0.5,0,-0.5,-(3**(1/2))/2,-1,-(3**(1/2))/2,-0.5,0,0.5,(3**(1/2))/2]

#scale down to fit window size
scale_down = 2.5

#translate unit circle to make all values positive and centered in the window
translation = 1.25

stddraw.setFontSize(32)

#translates and scales the position on the unit circle to be displayed properly in the window
def point_to_scale(point):
    return (point + translation)/scale_down

#scales the position down of the end point where the hand is drawn to, this makes the length shorter/longer
def hand_end_point(point, hour_hand):
    #each hands scale down factor is multiple of scale_down and translation to insure proper scaling
    if hour_hand:
        #scales the hour hand down by radius of clock/2
        return (point + 2.5)/5
    else:
        #scales the minute hand down by radius of clock/1.5
        return (point + 1.875)/3.75

#loop to make clock animate
while True:
    stddraw.clear()
    stddraw.setPenRadius(0.007)
    #draw clock borders
    stddraw.circle(0.5,0.5,0.48)
    stddraw.circle(0.5,0.5,0.45)

    #draw in numbers
    for i in range (12):
        stddraw.text(point_to_scale(x_value_unit_circle[i]),point_to_scale(y_value_unit_circle[i]), str(i) if not i == 0 else "12")

    #get current time
    time_aggregate = datetime.datetime.now()
    hour = time_aggregate.hour
    minute = time_aggregate.minute
    second = time_aggregate.second

    stddraw.text(0.1,0.95,str(hour) + ":" + str(minute) + ":" + str(second))

    #get end point of each hand on unit circle relative to the starting point of (0,1) on the unit circle
    radian_angle_seconds = ((second * 6) * math.pi)/180 #convert degrees to rads
    posx = ((point_to_scale(0) - 0.5)*math.cos(radian_angle_seconds) + (point_to_scale(1) - 0.5)*math.sin(radian_angle_seconds)) + 0.5
    posy = (-(point_to_scale(0) - 0.5)*math.sin(radian_angle_seconds) + (point_to_scale(1) - 0.5)*math.cos(radian_angle_seconds)) + 0.5
    #red second hand, normal length and width
    stddraw.setPenColor(stddraw.RED)
    stddraw.line(0.5,0.5,posx,posy)

    radian_angle_minutes = ((minute * 6) * math.pi)/180 #convert degrees to rads
    posx = ((hand_end_point(0, False) - 0.5)*math.cos(radian_angle_minutes) + (hand_end_point(1, False) - 0.5)*math.sin(radian_angle_minutes)) + 0.5
    posy = (-(hand_end_point(0, False) - 0.5)*math.sin(radian_angle_minutes) + (hand_end_point(1, False) - 0.5)*math.cos(radian_angle_minutes)) + 0.5
    #blue minute hand, shorter length and more width
    stddraw.setPenRadius(0.0095)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.line(0.5,0.5,posx,posy)

    #black hour hand, shortest length and most width
    radian_angle_hours = (((hour * 30) + (minute*0.6)) * math.pi)/180 #convert degrees to rads, add degrees of minutes so hour hand can accurately tell time
    posx = ((hand_end_point(0, True) - 0.5)*math.cos(radian_angle_hours) + (hand_end_point(1, True) - 0.5)*math.sin(radian_angle_hours)) + 0.5
    posy = (-(hand_end_point(0, True) - 0.5)*math.sin(radian_angle_hours) + (hand_end_point(1, True) - 0.5)*math.cos(radian_angle_hours)) + 0.5
    stddraw.setPenRadius(0.0125)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(0.5,0.5,posx,posy)

    #point in middle
    stddraw.setPenRadius(0.016)
    stddraw.point(0.5,0.5)
    stddraw.show(100)
