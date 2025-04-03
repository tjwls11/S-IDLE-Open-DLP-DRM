from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_postgres_db, get_sqlite_db
from sqlalchemy.sql import text

app = FastAPI(title="DRM API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 루트 엔드포인트
@app.get("/")
def root():
    return {"message": "Open DRM"}

# Favicon 처리
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {}

# PostgreSQL 연결 테스트
@app.get("/test-postgres-db")
def test_postgres_db_connection(db: Session = Depends(get_postgres_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "PostgreSQL 연결 성공"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PostgreSQL 연결 실패: {str(e)}")

# SQLite 연결 테스트
@app.get("/test-sqlite-db")
def test_sqlite_db_connection(db: Session = Depends(get_sqlite_db)):
    try:
        result = db.execute(text("SELECT sqlite_version();")).fetchone()
        return {"message": "SQLite 연결 성공", "version": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SQLite 연결 실패: {str(e)}")
    