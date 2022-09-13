from fastapi import FastAPI
from Router import blog_get
from Router import blog_post


app = FastAPI()
app.include_router(blog_get.app)
app.include_router(blog_post.app)


@app.get("/", tags=["Home Page"], summary="This is the home page")
def welcome():
    return {"message": 'Welcome to the new api'}


""" 
operation and discriptins

1 status code
2 Tag
3 Summary and description 
4 Response description


"""
