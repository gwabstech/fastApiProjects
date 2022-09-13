from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

#path and queryparams


@app.get("/blog/all")
def get_all_blogs(page: int = 1, pageSize: Optional[int] = 1):
    return {"message": f"All blogs retuned for page {page}  size {pageSize}"}


@app.get("/")
def welcome():
    return {"message": 'Welcome to the new api'}


# path parameters
@app.get("/spesific_blog/{id}")
def get_blog(id: int):
    return {"message": f"blog number {id}"}


@app.get("/blog/{page}")
def gt1(page: int, pageSize: int = 1):
    return {"message": f"the page is {page} and the size is {pageSize}"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howTo = "howTo"


@app.get("/blog/type/{type}")
def getBlogType(type: BlogType):
    return {"messge": f"Blog type {type}"}


@app.get("/blog/{id}/comments/{comment_id}")
def getComment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid},username {username}'}
