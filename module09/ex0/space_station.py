from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
        model for space station data with validation
    """
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True



class CurrentWeather(BaseModel):
    temperature: float = Field(alias="temperature_2m")
    windspeed: float = Field(alias="wind_speed_10m")
    time: datetime
 
    class Config:
        populate_by_name = True


class DailyWeather(BaseModel):
    time: list[str] = Field(..., min_length=7, max_length=7)
    temperature_max: list[float] = Field(alias="temperature_2m_max")
    temperature_min: list[float] = Field(alias="temperature_2m_min")
    precipitation_sum: list[float] = Field(...)

    class Config:
        populate_by_name = True


class AmsterdamWeeklyWeather(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    current: CurrentWeather
    daily: DailyWeather

def showWeather() -> None:
    import requests

    print("\nWeather report for this week")

    url = "https://api.open-meteo.com/v1/forecast?latitude=52.37&longitude=4.89&current=temperature_2m,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Amsterdam&forecast_days=7"

    try:
        data = requests.get(url).json() 
        weather = AmsterdamWeeklyWeather(**data)

        print(f"\n📍 Current: {weather.current.temperature}°C,"
              f"Wind: {weather.current.windspeed} km/h")
        print(f"\n📅 7-Day Forecast:")
        for i in range(len(weather.daily.time)):
            print(f"{weather.daily.time[i]}: "
                  f"{weather.daily.temperature_min[i]}°C - "
                  f"{weather.daily.temperature_max[i]}°C, "
                  f"Rain: {weather.daily.precipitation_sum[i]}mm")
    except Exception as e:
        print(f"problem fetching data: {e}")

def showSpaceStation() -> None:
    print("\nspace station data validation")

    try:
        station = SpaceStation(
            station_id="iss001",
            name="international space station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30)
        )

        print("\nvalid station created:")
        print(f"id: {station.station_id}")
        print(f"name: {station.name}")
        print(f"crew: {station.crew_size} people")
        print(f"power: {station.power_level}%")
        print(f"oxygen: {station.oxygen_level}%")
        print(f"status: {'operational' if station.is_operational else 'non-operational'}")

    except ValidationError as e:
        print(f"validation error: {e}")

    print("\nattempting to create invalid station (crew_size > 20)...")

    try:
        invalid_station = SpaceStation(
            station_id="iss002",
            name="invalid station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print("expected validation error:")
        for error in e.errors():
            if error['loc'][0] == 'crew_size':
                print(error['msg'])


if __name__ == "__main__":

    showSpaceStation()

    showWeather()


