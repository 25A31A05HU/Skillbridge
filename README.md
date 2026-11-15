# SkillBridge: Empowering Rural Artisans

SkillBridge is a multilingual, voice-enabled web platform designed to empower rural artisans across India. By leveraging browser-based speech recognition in **Telugu, Hindi, and English**, artisans can easily register their traditional crafts and services. The platform features an automated fair pricing calculator that ensures transparent, itemized payouts that value traditional labor fairly.

---

## ✨ Key Features

- **🎙️ Multilingual Voice Registration:** Built with the Browser Web Speech API to parse voice input and text descriptions in Telugu (`te-IN`), Hindi (`hi-IN`), and English (`en-IN`).
- **🛠️ 15 Rural Job Categories:** Automatically maps spoken or typed keywords to specific craft categories (such as Tailoring, Handloom Weaving, Home-Cooked Food, Pottery, Bamboo Crafts, Folk Painting, and Organic Farming).
- **💰 Transparent Fair Pricing Calculator:** Itemizes financial breakdowns including raw material reimbursement, skill complexity multipliers, direct artisan payout, and a transparent 5% platform upkeep fee.
- **⚡ Modern Responsive UI:** Styled with Tailwind CSS for a clean, mobile-friendly experience.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, REST APIs
- **Frontend:** HTML5, Tailwind CSS (via CDN)
- **Voice Recognition:** Web Speech API (Chrome / modern web browsers)

---

## 📁 Project Structure

```text
skillbridge/
│
├── app.py               # Flask backend, routing, and job profile logic
├── templates/
   └── index.html       # Frontend UI, voice recognition, and pricing calculator
