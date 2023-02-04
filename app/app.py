from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from collections import namedtuple

from faker import Faker

app = FastAPI()
templates = Jinja2Templates('../public')

app.mount("/public", StaticFiles(directory="../public"), name="public")

faker = Faker()
Course = namedtuple('Course', ['image_url', 'name', 'modules', 'author'])

@app.get('/')
async def home(request: Request):
    courses = [Course(faker.image_url(), faker.language_name(), faker.numerify('%# Modules'), faker.first_name_nonbinary()) for _ in range(6)]

    
    # print(images)
    return templates.TemplateResponse('index.html', {'request': request, 'courses': courses})
