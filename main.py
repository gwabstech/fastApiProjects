from enum import Enum
from tokenize import String
from typing import Optional, Union

from fastapi import FastAPI

app = FastAPI()

#path and queryparams
@app.get("/blog/all")
def get_all_blogs(page:int = 1,pageSize:Optional[int] = 1):
    return {"message": f"All blogs retuned for page {page}  size {pageSize}"}

@app.get("/blog/{page}")
def gt1(page:int,pageSize:int = 1):
    return {"message": f"the page is {page} and the size is {pageSize}"}

class BlogType(str,Enum):
    short="short"
    story="story"
    howTo="howTo"
@app.get("/blog/type/{type}")
def getBlogType(type:BlogType):
    return {"messge":f"Blog type {type}"}

@app.get("/blog/{id}")
def get_glog(id: int):
    return {"message": f"blog number {id}"}
