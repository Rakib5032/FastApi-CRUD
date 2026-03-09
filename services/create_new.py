from database.database import cursor, conn
from schema.user_input import Student
from fastapi.exceptions import HTTPException
import sqlite3

def create_student(student: Student):
    if(
        student.name.lower() == 'string' or
        student.email.lower() == 'user@example.com' or
        student.password.lower == 'string' or
        student.dept.lower == 'string' or
        student.phone.lower() == 'string' or
        student.address.lower() == 'string' 
    ):
        raise HTTPException(status_code=400, detail='Invalid placeholder data')
    
    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",(student.student_id,)
    )
    
    if cursor.fetchone():
        raise HTTPException(status_code=404, detail='Student already Exist with this ID')
        
    try:
        cursor.execute(
            """
            INSERT INTO students(student_id, name, email, password, dept, year, phone, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (
                student.student_id,
                student.name,
                student.email,
                student.password,
                student.dept,
                student.year,
                student.phone,
                student.address
            )
        )

        conn.commit()
        return {'Message': 'Student Created Successfully'}
    
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))
