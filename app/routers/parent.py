from fastapi import FastAPI, Response,status,HTTPException,APIRouter
from ..schemas import *
from ..db_auth import auth

router = APIRouter(prefix="/parent",tags=['parent'])

cursor,conn = auth()

app = FastAPI()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_content(abc: parent):
    cursor.execute("""INSERT INTO parent (first_name, last_name) VALUES (%s, %s) RETURNING * """,(abc.first_name,
    abc.last_name))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@router.get("/{id}")
def get_id_content(id:int, response: Response):
    cursor.execute("""SELECT first_name, last_name FROM parent WHERE parent_id = %s""", (str(id)))
    find_post = cursor.fetchone()
    print(find_post)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"this post with post id {id} not found")

    return {"data": find_post}