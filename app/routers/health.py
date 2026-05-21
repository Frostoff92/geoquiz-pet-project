from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("/live")
def live_check():
    return {
        "status": "alive"
    }

@router.get("/ready")
def readiness_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }
    
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="DB unavailable"
        )