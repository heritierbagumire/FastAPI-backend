from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from .. import utils, oauth2
from ..schemas import *
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users",tags=["Users"])

app = FastAPI()


@router.get("/")
def users_list(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    data = db.query(models.User).all()
    return data

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=User_response)
def user_id(id:int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    data = db.query(models.User).filter(models.User.user_id==id).first()
    return data

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=User_response)
def create_user(abc: User, db: Session = Depends(get_db)):
    hashed_password = utils.hash(abc.password)
    abc.password = hashed_password
    data = models.User(**abc.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@router.delete("/{id}",status_code=status.HTTP_404_NOT_FOUND)
def delete_user(id:int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    data = db.query(models.User).filter(models.User.user_id==id)
    if data.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"post with id: {id} does not exist")
    data.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)