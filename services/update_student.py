from database.database import cursor, conn
from fastapi import HTTPException
import sqlite3


def update_info(student_id: str, student):

    # check if student exists
    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="Student not found")

    # get only provided fields
    update_data = student.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    fields = ", ".join([f"{key}=?" for key in update_data.keys()])
    values = list(update_data.values())

    query = f"UPDATE students SET {fields} WHERE student_id=?"

    try:
        cursor.execute(query, values + [student_id])
        conn.commit()

    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")

    return {"message": "Student updated successfully"}