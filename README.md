# Guardian — Simple Telegram Moderation Bot

Minimal **group moderation bot** written with
`python-telegram-bot==13.15`

Botning vazifasi:
Admin messagega **reply qilib `/ban` yozsa** — o‘sha user groupdan chiqariladi.

---

## Texnologiyalar

* Python 3.9+
* python-telegram-bot 13.15
* python-dotenv
* JSON (logging uchun)

---

## 1. Bot yaratish

1. Telegram’da **@BotFather** ga kiring
2. `/newbot` yuboring
3. Nom va username tanlang
4. Token oling

Token quyidagiga o‘xshaydi:

```
123456789:AAHXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 2. Loyihani yuklash

```bash
git clone <repo>
cd guardian
```

---

## 3. Virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

---

## 4. Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## 5. .env sozlash

`.env` fayl yarating:

```
BOT_TOKEN=YOUR_TOKEN_HERE
```

---

## 6. Botni groupga qo‘shish

Botni groupga qo‘shing va admin qiling:

Group Settings → Administrators → Add Admin

**Muhim:**
Botda quyidagi huquqlar bo‘lishi kerak:

* Ban users
* Delete messages

---

## 7. Botni ishga tushirish

```bash
python run.py
```

---

## Qanday ishlaydi

1. User groupda message yozadi
2. Admin o‘sha messagega reply qiladi
3. `/ban` yozadi
4. Bot userni groupdan chiqaradi

---

## Misol

```
User: reklama
Admin: (reply) /ban
Bot: user banned
```

---

## Qoidalar

* `/ban` faqat groupda ishlaydi
* Replysiz ishlamaydi
* Oddiy user ishlata olmaydi
* Adminni ban qilib bo‘lmaydi

---

## Keyingi bosqichlar (o‘zingiz qo‘shib ko‘ring)

* ban reason
* temporary ban
* warn system
* mute

---

## Run checklist

* [ ] Bot token qo‘shildi
* [ ] Bot admin qilindi
* [ ] Groupda ishga tushdi
* [ ] Reply + /ban ishladi

---

Happy coding 🚀
