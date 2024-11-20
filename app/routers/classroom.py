from fastapi import FastAPI, Response,status,HTTPException,APIRouter
from ..schemas import *
from ..db_auth import auth



router = APIRouter(prefix="/classroom",tags=["Classroom"])

cursor,conn = auth()

app = FastAPI()


@router.get("/{id}")
def get_id_content(id: int, response: Response):
    cursor.execute("""SELECT * FROM classroom WHERE classroom_id = %s""", (str(id)))
    find_post = cursor.fetchone()
    print(find_post)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"this post with post id {id} not found")
       
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return f"the post with {id} not found"
        # print(find_post)
    return {"data": find_post}

@router.get("/")
def get_all_content():

    cursor.execute("""SELECT * FROM classroom """)
    posts = cursor.fetchall()
    return posts


@router.get("/latest")
def get_latest_content():

    # post = my_data[len(my_data)-1]
    cursor.execute("""SELECT * FROM classroom """)
    posts = cursor.fetchall()
    new_post = posts[-1]

    return {"detail": new_post}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_content(abc: classroom):
    cursor.execute("""INSERT INTO classroom (remarks, section, status, date) VALUES (%s, %s,%s, %s) RETURNING * """,(abc.remarks,
    abc.section,abc.status, abc.date))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@router.put("/{id}")
def update_content(id: int, abc: classroom):


    # index = find_index(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"the content with id {id} not exist")
    # print(post.dict())
    # content = post.dict()
    # content['classroom_id'] = id
    # my_data[index] = content

    cursor.execute("""UPDATE classroom SET remarks = %s, section = %s, status = %s, date = %s WHERE classroom_id = %s RETURNING * """,(abc.remarks, abc.section, abc.status, abc.date,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    return {"data": updated_post}

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id: int):
    cursor.execute("""DELETE FROM classroom WHERE classroom_id = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    # index = find_index(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id {id} does not exist")
    # my_data.pop(index)
    # return Response(status_code= status.HTTP_204_NO_CONTENT)

    return {"data": deleted_post}