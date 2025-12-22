# 🛒 Product Price Tracker

> แอปพลิเคชันเว็บสำหรับติดตามสินค้าที่ผู้ใช้สนใจ  
> ผู้ใช้สามารถกรอก URL ของสินค้า ระบบจะตรวจสอบข้อมูลและส่งอีเมลแจ้งเตือนเมื่อมีการเปลี่ยนแปลง

---

## ✨ Features
- 🔗 เพิ่มการติดตามสินค้าโดยการกรอก URL ของสินค้า (HTTP link)
- 🔄 ตรวจสอบสินค้าที่ติดตามโดยอัตโนมัติ
- 📧 ส่งอีเมลแจ้งเตือนเมื่อข้อมูลสินค้ามีการเปลี่ยนแปลง
- 🖥️ อินเทอร์เฟซใช้งานง่าย และเป็นมิตรกับผู้ใช้

---

## 🛠️ Tech Stack
- **Backend:** Django  
- **Frontend:** React  
- **Database:** SQLite 

---
## Others:
- REST API
- Background Tasks (Scheduled Jobs)
- Email Notification (SMTP)
- Environment Variables (.env)


## ⚙️ How It Works
1. ผู้ใช้กรอก URL ของสินค้าผ่านหน้าเว็บ
2. Backend ประมวลผลและจัดเก็บข้อมูลสินค้า
3. ระบบตรวจสอบการเปลี่ยนแปลงของข้อมูลสินค้าเป็นระยะ
4. ส่งอีเมลแจ้งเตือนไปยังผู้ใช้เมื่อพบการเปลี่ยนแปลง

---

### Get started 


### Backend
```bash
cd backend
python mange.py runserver 
```

### Frontend
```bash
cd frontend
npm install
npm run dev
``` 

## 📚 What I Learned
- การพัฒนา REST API ด้วย Django
- การเชื่อมต่อ Frontend (React) กับ Backend (Django)
- การจัดการ background tasks และระบบแจ้งเตือนผ่านอีเมล
- การออกแบบ workflow สำหรับระบบติดตามสินค้าแบบง่าย

---

## 🚀 Future Improvements
- รองรับหลายเว็บไซต์ E-commerce
- ตั้งเงื่อนไขแจ้งเตือนตามราคาที่ผู้ใช้กำหนด
- เพิ่มระบบสมาชิกและประวัติการติดตามสินค้า
