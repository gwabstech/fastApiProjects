from fastapi import APIRouter

app = APIRouter(
    prefix="/blog",
    tags=["blog"]

)


@app.post('/')
def create_blog():
    return {'message': "blog created"}
    pass
