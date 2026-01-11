from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator

class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True

class SpaceMission(BaseModel):

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self):

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

 
        leadership_ranks = {Rank.commander, Rank.captain}
        if not any(member.rank in leadership_ranks for member in self.crew):
            raise ValueError("Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = [
                member for member in self.crew if member.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% experienced crew"
                )

        inactive = [member.name for member in self.crew if not member.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active (inactive: {', '.join(inactive)})"
            )

        return self

if __name__ == "__main__":
    print("\nSpace Mission Crew Validation")
    print("=" * 40)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 10, 1),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20,
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=34,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=29,
                    specialization="Engineering",
                    years_experience=5,
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) - {member.specialization}"
            )

    except ValidationError as e:
        print("Unexpected validation error:")
        print(e)

    print()
    print("=" * 40)

    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_AST",
            mission_name="Asteroid Survey",
            destination="Asteroid Belt",
            launch_date=datetime(2025, 5, 20),
            duration_days=120,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="C010",
                    name="Bob Lee",
                    rank=Rank.officer,
                    age=32,
                    specialization="Science",
                    years_experience=6,
                ),
                CrewMember(
                    member_id="C011",
                    name="Eva Green",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Operations",
                    years_experience=7,
                ),
            ],
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])



