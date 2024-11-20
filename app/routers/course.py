from fastapi import FastAPI, Response,status,HTTPException,APIRouter
from ..schemas import *
from ..db_auth import auth


router = APIRouter(prefix="/course",tags=["Course"])

cursor,conn = auth()

app = FastAPI()

@router.get("/{id}")
def get_id_content(id:int, response: Response):
    cursor.execute("""SELECT * FROM course WHERE course_id = %s""", (str(id)))
    find_post = cursor.fetchone()
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"this post with post id {id} not found")

    return {"data": find_post}

@router.get("/")
def get_all_content():
    cursor.execute("""SELECT * FROM course""")
    posts = cursor.fetchall()
    return {"data": posts}

@router.post("/",status_code = status.HTTP_201_CREATED)
def create_content(abc: Course):
    cursor.execute("""INSERT INTO course (description, name) VALUES (%s, %s) RETURNING *""", (abc.description, abc.name))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data': new_post}
    
@router.put("/{id}")
def update_id(id: int, abc: Course):
    cursor.execute("""UPDATE course SET description = %s, name = %s WHERE course_id = %s RETURNING * """,(abc.description, abc.name,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    return {"data": updated_post}

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id: int):
    cursor.execute("""DELETE FROM course WHERE course_id = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    return {"data": deleted_post}

