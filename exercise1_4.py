overtime = 40
def computepay(hours, rate):
    if hours >= overtime:
        return (hours * rate) + ((hours-overtime) * (rate * 0.5))
    else:
        return (hours * rate)

#print(computepay(45,10))
