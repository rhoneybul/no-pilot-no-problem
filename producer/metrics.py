import random

def fetch_height(x, duration, takeoff_interval, height_coeff):
    if x < takeoff_interval or duration - x < takeoff_interval:
        return 0
    else:
        return - (1 / height_coeff) * (x - takeoff_interval) * (x - (duration - takeoff_interval))

def fetch_speed(x, duration, takeoff_interval, takeoff_speed, speed_var):
    if x < takeoff_interval:
        return (x**2) * (takeoff_speed / takeoff_interval**2)
    if x > (duration - takeoff_interval):
        return ((x - duration) ** 2) * (takeoff_speed / takeoff_interval ** 2)
    if x == duration:
        return 0
    return takeoff_speed + random.randint(0, speed_var / 2)

def fetch_metrics(x, duration, takeoff_interval, takeoff_speed, speed_var, height_coeff):

    height = fetch_height(x, duration, takeoff_interval, height_coeff)
    speed = fetch_speed(x, duration, takeoff_interval, takeoff_speed, speed_var)

    return {
        "height": height,
        "speed": speed
    }