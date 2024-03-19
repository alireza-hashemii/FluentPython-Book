class Bird:
    pass


class Duck(Bird): 
    def quack(self):
        print('Quack!')

def alert(birdie): 
    birdie.quack()

def alert_duck(birdie: Duck) -> None: 
    birdie.quack()


def alert_bird(birdie: Bird) -> None: 
    birdie.quack()


# type hints for tuples

from geolib import geohash as gh

PRECISION = 9

def geohash(lat_lon: tuple[float, float]) -> str: 
    return gh.encode(*lat_lon, PRECISION)

print(geohash((3632.4525,56517.8111)))