from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

app = APIRouter(
    prefix="/blog",
    tags=["blog"]

)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@app.post('/newBlog/{id}')
def create_blog(blog: BlogModel,  id: int, version: int = 1):
    return {"data": blog}, {"message": f"Blog created with id {id} of version: {version}"}
    pass
