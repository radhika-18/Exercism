def getminutes(minutes):
    hourct=0
    mod=abs(minutes)
    while mod>=60:
        mod=minutes%60
        temp=abs(minutes)
        while temp>=60:
            temp/=60
            hourct+=1
    return [hourct,mod]

def gethours(hours,ct):
    if hours+ct>0:
        hours+=ct
    else:
        hours-=ct
    mod=hours%24
    if hours<0:
        return 24-mod-1
    else:
        return mod

class Clock:
    def __init__(self, hour, minutes):
        result=getminutes(minutes)
        self.minutes=result[1]
        self.hour=gethours(hour,result[0])

    def __str__(self):
        return "%02d"%(self.hour)+":"+"%02d"%(self.minutes)


# print str(Clock(8, 0))
# print str(Clock(11, 9))
# print str(Clock(24, 0))
# print str(Clock(25, 0))
# print str(Clock(100, 0))
# print str(Clock(1, 60))
print str(Clock(0, 160))
print str(Clock(0, 1723))
print str(Clock(25, 160))
print str(Clock(201, 3001))
print str(Clock(72, 8640))
print str(Clock(-1, 15))
print str(Clock(-25, 0))
print str(Clock(-91, 0))
print str(Clock(1, -40))
print str(Clock(1, -160))
print str(Clock(-25, -160))
print str(Clock(1, -4820))
print str(Clock(-121, -5810))

