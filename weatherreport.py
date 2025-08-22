def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def sensorStubHighPrecipLowWind():
    return {
        'temperatureInC': 50,
        'precipitation': 70,   # High precipitation (>60)
        'humidity': 26,
        'windSpeedKMPH': 40    # Low wind speed (<50)
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # Use the new stub to expose the bug
    weather = report(sensorStubHighPrecipLowWind)
    print(weather)
    # The function should NOT return "Sunny Day" for high precipitation
    assert("rain" in weather or "Cloudy" in weather or weather != "Sunny Day")


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
