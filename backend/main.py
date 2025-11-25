from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_models
from database import engine, SessionLocal
from models import Product

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Create table if not exist
database_models.Base.metadata.create_all(bind=engine)

#Sample data to initialize Db(pydentic objects)
products = [
    Product(id=1, name="Mobile", description="Samsung S24 Ultra", price=120000, quantity=3),
    Product(id=2, name="Laptop", description="hp PAVILION GAMING", price=80000, quantity=2),
    Product(id=3, name="Charger", description="Mobile Charger", price=2000, quantity=1),
    Product(id=4, name="Headphone", description="Boat Rokerz 255", price=1500, quantity=3),
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
def init_db():
    db = SessionLocal()
    try:
        count = db.query(database_models.Product).count()
        if count == 0:
            for product in products:
                data = product.model_dump() ## use p.model_dump() if pydantic v2
                db.add(database_models.Product(**data))
            db.commit()
    finally:
        db.close()

init_db()


@app.get("/")
def greeting():
    return "Welcome to Product Management System!"

@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", status_code=201)
def add_product(product: Product, db: Session = Depends(get_db)):
    existing = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product with this id already exists.")
    db_obj = database_models.Product(**product.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

@app.put("/products/{id}")
def update_product(id: int,product: Product, db: Session= Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="product not found.")
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{id}")
def delete_product(id: int, db: Session= Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="product not found.")
    
    db.delete(db_product)
    db.commit()
    return {"detail" : "product deleted"}

