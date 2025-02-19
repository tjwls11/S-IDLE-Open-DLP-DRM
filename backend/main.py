from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database  # import 방식 수정
import models
from pydantic import BaseModel  # 입력 데이터 검증을 위한 Pydantic 모델 추가

# FastAPI 앱 생성
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

# 의존성 주입: DB 세션
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 기본 API
@app.get("/")
def read_root():
    return {"message": "Open DRM/DLP"}

# 특정 아이템 조회
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

# 🔹 새로운 아이템 추가 API (POST 요청)
class ItemCreate(BaseModel):
    name: str

@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = models.Item(name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item