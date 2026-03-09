from database.database import cursor, conn
from fastapi.exceptions import HTTPException

def delete_student(student_id: str):
    cursor.execute(
        """
        SELECT * FROM students WHERE student_id=?
        """,(student_id,)
    )
    
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail='Student Not found')
    cursor.execute(
        "DELETE FROM students WHERE student_id=?",(student_id,)
    )
    
    conn.commit()
    return {'Message':'Student Deleted Successfully'}