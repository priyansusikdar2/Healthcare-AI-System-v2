from sqlalchemy.orm import Session
from typing import List
from app.models import findings
from app.schemas.findings_schema import FindingsCreate, FindingsUpdate

def create_finding(db: Session, finding: FindingsCreate):
    db_finding = findings.Findings(**finding.dict())
    db.add(db_finding)
    db.commit()
    db.refresh(db_finding)
    return db_finding

def get_finding(db: Session, finding_id: int):
    return db.query(findings.Findings).filter(findings.Findings.id == finding_id).first()

def get_findings(db: Session, skip: int = 0, limit: int = 100) -> List[findings.Findings]:
    return db.query(findings.Findings).offset(skip).limit(limit).all()

def update_finding(db: Session, finding_id: int, updates: FindingsUpdate):
    db_finding = get_finding(db, finding_id)
    if db_finding:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_finding, key, value)
        db.commit()
        db.refresh(db_finding)
    return db_finding

def delete_finding(db: Session, finding_id: int):
    db_finding = get_finding(db, finding_id)
    if db_finding:
        db.delete(db_finding)
        db.commit()
    return db_finding