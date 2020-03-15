EARTH_SECS = 31557600

PLANETS = {
  "earth": 1,
  "mercury": 0.2408467,
  "venus": 0.61519726,
  "mars": 1.8808158,
  "jupiter": 11.862615,
  "saturn": 29.447498,
  "uranus": 84.016846,
  "neptune": 164.79132
}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        for planet in PLANETS:
            setattr(self, f'on_{planet}', self.__value(planet))

    def value(self, planet):
        return lambda: round(self.seconds / (EARTH_SECS * PLANETS[planet]), 2)

    __value = value
