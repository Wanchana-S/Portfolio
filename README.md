# Portfolio Website - Flask + Python

เว็บไซต์ Portfolio ส่วนตัวที่พัฒนาด้วย Flask และ Python พร้อม UI ที่สวยงามและใช้งานง่าย

## 🚀 คุณสมบัติ

- **หน้าแรก** - แสดงข้อมูลสรุปและทักษะ
- **เกี่ยวกับฉัน** - ประวัติ ประสบการณ์ และการศึกษา
- **โปรเจ็ค** - แสดงผลงานและโปรเจ็คที่พัฒนา
- **ติดต่อ** - ฟอร์มติดต่อและข้อมูลการติดต่อ
- **Responsive Design** - รองรับทุกขนาดหน้าจอ
- **Modern UI/UX** - ดีไซน์ที่ทันสมัยและใช้งานง่าย
- **Interactive Elements** - เอฟเฟกต์และแอนิเมชัน

## 🛠️ เทคโนโลยีที่ใช้

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Database**: SQLite (สำหรับเก็บข้อมูล)

## 📁 โครงสร้างโปรเจ็ค

```
Portfolio/
├── app.py                 # ไฟล์หลัก Flask application
├── requirements.txt       # Python dependencies
├── README.md             # ไฟล์อธิบายโปรเจ็ค
├── static/               # ไฟล์ static
│   ├── css/
│   │   └── style.css     # Custom CSS
│   └── js/
│       └── script.js     # Custom JavaScript
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # หน้าแรก
    ├── about.html        # หน้าประวัติ
    ├── projects.html     # หน้าปรเจ็ค
    └── contact.html      # หน้าติดต่อ
```

## 🚀 วิธีการติดตั้งและรัน

### 1. ติดตั้ง Python และ pip
ตรวจสอบว่ามี Python 3.7+ ติดตั้งแล้ว

### 2. Clone หรือ Download โปรเจ็ค
```bash
cd "C:\Users\wanch\OneDrive\เดสก์ท็อป\LearningPython\Portfolio"
```

### 3. สร้าง Virtual Environment (แนะนำ)
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 5. รันแอปพลิเคชัน
```bash
python app.py
```

### 6. เปิดเบราว์เซอร์
ไปที่ `http://localhost:5000`

## 📝 การปรับแต่ง

### 1. แก้ไขข้อมูลส่วนตัว
แก้ไขข้อมูลใน `app.py` ในส่วน `portfolio_data`:

```python
portfolio_data = {
    'name': 'ชื่อของคุณ',
    'title': 'ตำแหน่งงาน',
    'about': 'ข้อมูลเกี่ยวกับตัวคุณ',
    'skills': ['ทักษะ1', 'ทักษะ2', ...],
    'projects': [
        {
            'title': 'ชื่อโปรเจ็ค',
            'description': 'รายละเอียดโปรเจ็ค',
            'technologies': ['เทคโนโลยี1', 'เทคโนโลยี2'],
            'image': 'รูปภาพโปรเจ็ค'
        }
    ],
    'contact': {
        'email': 'อีเมลของคุณ',
        'phone': 'เบอร์โทรศัพท์',
        'github': 'ลิงก์ GitHub',
        'linkedin': 'ลิงก์ LinkedIn'
    }
}
```

### 2. เพิ่มรูปภาพ
- วางรูปภาพในโฟลเดอร์ `static/images/`
- อ้างอิงใน HTML: `{{ url_for('static', filename='images/your-image.jpg') }}`

### 3. ปรับแต่ง CSS
แก้ไขไฟล์ `static/css/style.css` เพื่อปรับแต่งสีและสไตล์

### 4. เพิ่มหน้าใหม่
1. สร้างไฟล์ HTML ใน `templates/`
2. เพิ่ม route ใน `app.py`
3. เพิ่มลิงก์ใน navigation

## 🎨 หน้าต่างๆ

### หน้าแรก (/)
- Hero section พร้อมข้อมูลสรุป
- แสดงทักษะและเทคโนโลยี
- โปรเจ็คเด่น 3 อันดับแรก
- Call-to-action สำหรับติดต่อ

### เกี่ยวกับฉัน (/about)
- ข้อมูลส่วนตัวและประวัติ
- ทักษะแบ่งตามหมวดหมู่
- ประสบการณ์การทำงาน (Timeline)
- ข้อมูลการศึกษาและใบรับรอง

### โปรเจ็ค (/projects)
- แสดงโปรเจ็คทั้งหมด
- หมวดหมู่โปรเจ็ค
- สถิติและตัวเลข
- Modal สำหรับดูรายละเอียด

### ติดต่อ (/contact)
- ข้อมูลการติดต่อ
- ฟอร์มส่งข้อความ
- FAQ
- เวลาทำงาน

## 🔧 การพัฒนาเพิ่มเติม

### เพิ่มฐานข้อมูล
```python
# ใน app.py
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    # เพิ่มฟิลด์อื่นๆ
```

### เพิ่มระบบ Admin
```python
# ติดตั้ง Flask-Admin
pip install flask-admin

# ใน app.py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='Portfolio Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Project, db.session))
```

### เพิ่มระบบ Blog
```python
# สร้างโมเดล Blog
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## 📱 Responsive Design

เว็บไซต์รองรับทุกขนาดหน้าจอ:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: < 768px

## 🚀 Deployment

### Heroku
1. สร้างไฟล์ `Procfile`:
```
web: gunicorn app:app
```

2. ติดตั้ง gunicorn:
```bash
pip install gunicorn
```

3. Deploy ไปยัง Heroku

### Vercel
1. สร้างไฟล์ `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

## 🤝 การมีส่วนร่วม

1. Fork โปรเจ็ค
2. สร้าง Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit การเปลี่ยนแปลง (`git commit -m 'Add some AmazingFeature'`)
4. Push ไปยัง Branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## 📄 License

โปรเจ็คนี้อยู่ภายใต้ MIT License - ดูไฟล์ [LICENSE](LICENSE) สำหรับรายละเอียด

## 📞 ติดต่อ

หากมีคำถามหรือข้อเสนอแนะ สามารถติดต่อได้ที่:
- Email: wanchana.job@hotmail.com
- GitHub: [github.com/Wanchana-S](https://github.com/Wanchana-S)

---

**สร้างด้วย ❤️ โดยใช้ Flask และ Python** 
