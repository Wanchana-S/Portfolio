from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# ข้อมูล Portfolio
portfolio_data = {
    'name': 'Wanchana Portfolio',
    'title': 'ERP Developer & Business Applications Developer',
    'about': 'ฉันเป็นนักพัฒนาที่มีความเชี่ยวชาญในการพัฒนา ERP Systems และ Business Applications ด้วยประสบการณ์ในการพัฒนาแอปพลิเคชันด้วย C#, VB.NET, Angular และ JavaScript รวมถึงการทำงานกับฐานข้อมูล Microsoft SQL Server และ Oracle',
    'skills': [
        'C#', 'VB.NET', 'JavaScript', 'TypeScript', 'HTML/CSS', 'Angular', 'Bootstrap', 
        'Python', 'React', 'Microsoft SQL Server', 'Oracle', 'SSRS', 'SQL Queries', 
        'Stored Procedures', 'Performance Tuning', 'Visual Studio', 'Git', 'Sourcetree'
    ],
    # ลบ 'projects' ออก
    'contact': {
        'email': 'wanchana.job@hotmail.com',
        'phone': '092-278-0448',
        'line': 'raffyoreo',
        'address': '225/198 Soi 7 Sinthavee Greenville 2 Pracha Utid 90 Road Samut Prakan',
        'github': 'https://github.com/Wanchana-S',
        'linkedin': 'https://www.linkedin.com/in/wanchanalink',
        'facebook': 'https://facebook.com/wanch.portfolio',
        'twitter': 'https://twitter.com/wanch_portfolio'
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

# ลบ route /projects

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/contact', methods=['POST'])
def contact_submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            flash('ขอบคุณสำหรับข้อความ! ฉันจะติดต่อกลับโดยเร็วที่สุด', 'success')
        else:
            flash('กรุณากรอกข้อมูลให้ครบถ้วน', 'error')
        
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
