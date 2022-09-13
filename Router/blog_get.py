from fastapi import APIRouter
from enum import Enum
from typing import Optional
from urllib import response
from fastapi import status, Response

app = APIRouter(
    prefix='/blog',
    tags=["blog"]
)

# queryparams
# Default values
# optional values


@app.get("/all")
def get_all_blogs(page: int = 1, pageSize: Optional[int] = 2):
    return {"message": f"All blogs retuned for page {page}  size {pageSize}"}

# path parameters


@app.get("/spesific_blog/{id}", status_code=status.HTTP_404_NOT_FOUND, summary="returns specific blog base on id ")
def get_blog(id: int, response: Response):
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f'blog {id} not found', "status": status.HTTP_404_NOT_FOUND}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog with id {id} ", "status": status.HTTP_200_OK}


@app.get("/{page}", description="this api call return a list of blogs with the page given in the request")
def gt1(page: int, pageSize: int = 1):
    return {"message": f"the page is {page} and the size is {pageSize}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howTo = "howTo"


@app.get("/type/{type}", )
def getBlogType(type: BlogType):
    return {"messge": f"Blog type {type}"}


# Quary and path params combinations
# optional and default value
@app.get("/{id}/comments/{comment_id}",
         response_description="This returns base on id and comments")
def getComment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid},username {username}'}
