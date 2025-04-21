from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut 
from passlib.context import CryptContext  # type: ignore

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_db():
    async with SessionLocal() as db:
        yield db

@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    username = user.username.strip().lower()
    
    result = await db.execute(select(User).filter(User.username == username))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash password
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.post("/login", response_model=UserOut)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    username = user.username.strip().lower()
    result = await db.execute(select(User).filter(User.username == username))
    db_user = result.scalars().first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    print(f"User Password: {user.password}")
    print(f"DB User Password (hashed): {db_user.password}")

    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return db_user
