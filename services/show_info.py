from database.database import cursor
from fastapi import HTTPException

def show_info(student_id):
    cursor.execute(
        " SELECT * FROM students WHERE student_id=?",(student_id,)
    )
    info = cursor.fetchone()
    if not info:
        raise HTTPException(status_code=404, detail='Student not found')
    return{
        'id':  info[0],
        'name': info[2],
        'student_id': info[1],
        'email': info[3],
        # 'password': info[4],
        'dept': info[5],
        'year': info[6],
        'phone': info[7],
        'address': info[8]
        }