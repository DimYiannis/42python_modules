from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError

class spacestation(BaseModel):
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
    notes: Optional[str] = Field(None, max_length=200)

if __name__ == "__main__":

    print("\nspace station data validation")

    try:
        station = spacestation(
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
        invalid_station = spacestation(
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

