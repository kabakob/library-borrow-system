#db_init.py
import sqlite3
# 1. เชื่อมต่อ (หรือสร้างไฟล์ถ้าไม่มี)
conn = sqlite3.connect("library.db")
c = conn.cursor()

# 2. สร้างตาราง books ถ้ายังไม่มี
c.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    status TEXT DEFAULT 'available'
)
""")

# 3. บันทึกการเปลี่ยนแปลง
conn.commit()
# 4. ปิดการเชื่อมต่อ
conn.close()

