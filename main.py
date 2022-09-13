from enum import Enum
from typing import Optional
from fastapi import FastAPI, status, Response

app = FastAPI()

# queryparams
# Default values
# optional values


@app.get("/blog/all", tags=["blog"])
def get_all_blogs(page: int = 1, pageSize: Optional[int] = 2):
    return {"message": f"All blogs retuned for page {page}  size {pageSize}"}


@app.get("/")
def welcome():
    return {"message": 'Welcome to the new api'}


# path parameters
@app.get("/spesific_blog/{id}", status_code=status.HTTP_404_NOT_FOUND, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f'blog {id} not found', "status": status.HTTP_404_NOT_FOUND}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog with id {id} ", "status": status.HTTP_200_OK}


@app.get("/blog/{page}", tags=["blog"])
def gt1(page: int, pageSize: int = 1):
    return {"message": f"the page is {page} and the size is {pageSize}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howTo = "howTo"


@app.get("/blog/type/{type}", tags=["blog"])
def getBlogType(type: BlogType):
    return {"messge": f"Blog type {type}"}


# Quary and path params combinations
# optional and default value
@app.get("/blog/{id}/comments/{comment_id}", tags=["Comments"])
def getComment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid},username {username}'}


""" 
operation and discriptins

1 status code
2 Tag
3 Summary and description 
4 Response description


"""

# Status code
