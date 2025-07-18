from sqlalchemy.orm import Session
from . import model, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = model.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(model.Product).filter(model.Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = db.query(model.Product).filter(model.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(model.Product).filter(model.Product.id == product_id).first()
    if db_product is None:
        return None
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return db_product

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = model.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(model.User).filter(model.User.username == username).first()

