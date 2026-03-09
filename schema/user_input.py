from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional

#for user data validation
class Student(BaseModel):
    student_id: Annotated[str, Field(..., title='ID of the Student', max_length=20, pattern=r"^[\d-]+$", examples=['221-15-5032'])]
    name: Annotated[str, Field(..., title='Name of the student')]
    email: EmailStr
    password: Annotated[str, Field(..., min_length=6)]
    dept: Annotated[str, Field(..., max_length=10)]
    year: Annotated[int, Field(..., ge=1, le=4)]
    phone: Annotated[str, Field(..., pattern="^[0-9]{11}$")]
    address: Annotated[str, Field(..., title='This is address of student')]

#for updating info of student
class UpdateStudentInfo(BaseModel):
    name: Annotated[
        Optional[str],
        Field(title="Name of the student")
    ] = None

    email: Optional[EmailStr] = None

    password: Annotated[
        Optional[str],
        Field(min_length=6)
    ] = None

    dept: Annotated[
        Optional[str],
        Field(max_length=10)
    ] = None

    year: Annotated[
        Optional[int],
        Field(ge=1, le=4)
    ] = None

    phone: Annotated[
        Optional[str],
        Field(pattern=r"^[0-9]{11}$")
    ] = None

    address: Annotated[
        Optional[str],
        Field(title="Address of student")
    ] = None
    


