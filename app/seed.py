import json

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import CountryModel

def seed_countries():
    db: Session = SessionLocal()

    existing_countries = db.query(CountryModel).count()

    if existing_countries > 0:
        print("Database already seeded.")
        db.close()
        return
    
    with open("app/data/countries.json", "r", encoding="utf-8") as file:
        countries = json.load(file)

    for country in countries:
        db_country = CountryModel(
            id=country["id"],
            name=country["name"],
            flag=country["flag"],
            difficulty=country["difficulty"],
            continent=country["continent"],
            capital=country["capital"],
            similar_to=country["similar_to"],
        )

        db.add(db_country)

    db.commit()
    db.close()

    print("Countries seeded successfully.")

if __name__ == "__main__":
    seed_countries()