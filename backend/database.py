from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL 설정 (구글 클라우드)
POSTGRES_DATABASE_URL = (
    f"postgresql+psycopg2://postgres:Ok%2AXVK5ScdVI%3Fed%5E@104.197.63.31:5432/drm"
    "?sslmode=require"
    "&sslcert=certs/client-cert.pem"
    "&sslkey=certs/client-key.pem"
    "&sslrootcert=certs/server-ca.pem"
)
postgres_engine = create_engine(POSTGRES_DATABASE_URL, echo=True)
PostgresSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)

# SQLite 설정 (로컬)
SQLITE_DATABASE_URL = "sqlite:///./local.db"
sqlite_engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
SqliteSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sqlite_engine)

# SQLAlchemy Base
Base = declarative_base()

# PostgreSQL용 세션                                                                                                                                                                                                                                                                                                            
def get_postgres_db():
    db = PostgresSessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLite용 세션
def get_sqlite_db():
    db = SqliteSessionLocal()
    try:
        yield db
    finally:
        db.close()

# 테이블 생성
Base.metadata.create_all(bind=postgres_engine)  # PostgreSQL 테이블 
Base.metadata.create_all(bind=sqlite_engine)    # SQLite 테이블 