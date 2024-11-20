from fastapi import FastAPI, Response,status,HTTPException,APIRouter
from ..schemas import *
from ..db_auth import auth


app = FastAPI()

cursor,conn = auth()

router = APIRouter(prefix="/exam_result",tags=['Exam_Result'])

@router.get("/{id}")
def get_id_content(id:int, response: Response):
    cursor.execute("""SELECT * FROM exam_result WHERE course_id = %s""", (str(id)))
    find_post = cursor.fetchone()
    print(find_post)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"this post with post id {id} not found")

    return {"data": find_post}

@router.get("/")
def get_all_content():
    cursor.execute("""SELECT * FROM exam_result""")
    posts = cursor.fetchall()
    return {"data": posts}

@router.post("/",status_code = status.HTTP_201_CREATED)
def create_content(abc: Exam_result):
    cursor.execute("""INSERT INTO exam_result (marks) VALUES (%s) RETURNING *""", (abc.marks))
    new_post = cursor.fetchone()
    conn.commmit()
    return {'data': new_post}
    
@router.put("/{id}")
def update_id(id: int, abc: Course):
    cursor.execute("""UPDATE exam_result SET marks = %s RETURNING * """,(abc.marks,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    return {"data": updated_post}

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id: int):
    cursor.execute("""DELETE FROM exam_result WHERE marks = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    return {"data": deleted_post}