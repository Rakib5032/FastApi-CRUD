from fastapi import FastAPI, Request, Form
from services.show_info import show_info
from schema.user_input import Student, UpdateStudentInfo
from services.create_new import create_student
from services.update_student import update_info
from services.delete_student import delete_student
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request})

#api
@app.get('/api/get/{student_id}')
def get_student_info(student_id):
    return show_info(student_id)

#Route for Student profile
@app.get("/students/{student_id}")
def student_profile(request: Request, student_id: str):

    student = show_info(student_id)

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "a": student
        }
    )
    
#api
@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )
    
@app.post('/api/register')
def create(student: Student):
    return create_student(student)

@app.put('/api/update/{student_id}')
def update(student_id: str, student: UpdateStudentInfo):
    return update_info(student_id, student)

@app.get('/update')
def update_user(request: Request):
    return templates.TemplateResponse(
        'update.html',
        {'request': request}
    )
@app.get('/delete')
def delete_user(request: Request):
    return templates.TemplateResponse(
        'delete.html',
        {'request': request}
    )

@app.delete('/api/delete/{student_id}')
def delete(student_id: str):
    return delete_student(student_id)