from fastapi import FastAPI, Depends, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware  
from fastApi import models


from fastApi.models import Folders
from fastApi.database import engine, SessionLocal
from typing import Annotated 
from sqlalchemy.orm import Session
from pydantic import BaseModel, StrictInt, Field
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db) ]

class FolderRequest(BaseModel):
    id: Optional[StrictInt] = None 
    title: str = Field(min_length=3)
    

@app.get("/folders")
async def read_all(db: db_dependency):
    return db.query(Folders).all()

@app.get("/folders/{folder_id}")
async def get_folder_by_id(db: db_dependency, folder_id: int = Path(gt=0)):
    folder_result = db.query(Folders).filter(Folders.id == folder_id).first()

    if folder_result is not None:
        return folder_result
    
    raise HTTPException(status_code=404, detail="Folder not found") 

@app.post("/folders/create_folder")
async def create_folder(db: db_dependency, folder_request: FolderRequest):
    folder = Folders(**folder_request.model_dump())
    db.add(folder)
    db.commit()

@app.put("/folders/{folder_id}")
async def update_folder(db: db_dependency,                        
                      folder_request: FolderRequest,
                      folder_id: int = Path(gt=0)):
    folder_result = db.query(Folders).filter(Folders.id == folder_id).first()
    if folder_result is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    
    folder_result.title = folder_request.title 
    
    
    db.add(folder_result)
    db.commit()

@app.delete("/folders/{folder_id}")
async def delete_folder(db: db_dependency, folder_id: int = Path(gt=0)):
    folder_result = db.query(Folders).filter(Folders.id == folder_id).first()

    if folder_result is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    else:
        db.query(Folders).filter(Folders.id == folder_id).delete()
    
    db.commit()
    