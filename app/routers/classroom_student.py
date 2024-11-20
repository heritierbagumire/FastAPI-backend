from fastapi import FastAPI, Response,status,HTTPException,APIRouter
from ..schemas import *
from ..db_auth import auth

app = FastAPI()
cursor,conn = auth()
router = APIRouter(prefix="/classroom_student",tags=["Classroom_student"])

@router.get("/{id}")
def get_id_content(id:int, response: Response):
    cursor.execute("""SELECT * FROM classroom_student WHERE classroom_stu_id = %s""", (str(id)))
    find_post = cursor.fetchone()
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"this post with post id {id} not found")

    return {"data": find_post}

@router.get("/")
def get_all_content():
    cursor.execute("""SELECT * FROM classroom_student""")
    posts = cursor.fetchall()
    return {"data": posts}


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id: int):
    cursor.execute("""DELETE FROM claassroom_student WHERE classroom_stu_id = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"this post with post id {id} not found")
    conn.commit()
    return {"data": deleted_post}