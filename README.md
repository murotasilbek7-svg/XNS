XNS Engine 🚀
XNS Engine — bu Python dasturlash tilida yozilgan, o'yin yaratishni o'rganuvchilar uchun mo'ljallangan yengil o'yin dvigateli. Ushbu engine grafika qismi uchun kuchli Ursina Engine kutubxonasidan foydalanadi.

Garchi bu professional darajadagi o'yinlar yaratish uchun mo'ljallanmagan bo'lsa-da, o'yin mantiqi, 3D modellar bilan ishlash va umumiy o'yin arxitekturasini o'rganish uchun juda qulay vositadir.

✨ Asosiy xususiyatlari:
Grafika: Ursina kutubxonasi yordamida tezkor renderlash.

Oson boshqaruv: Python tilini biladigan har qanday foydalanuvchi o'z o'yinini qisqa vaqtda yarata oladi.

Tayyor muhit: Kutubxonalarni qo'lda o'rnatish shart emas, barchasi sozlangan.

🛠 O'rnatish va Ishga tushirish
Dvigatelni ishga tushirish juda oson. Quyidagi qadamlarni bajaring:

Loyihani yuklab oling:

Bash

git clone https://github.com/murotasilbek7/xns.git
cd xns-engine
Dasturni ishga tushiring: Loyiha ichidagi run.bat faylini ikki marta bosing yoki terminal orqali ishga tushiring:

Bash

run.bat
[!IMPORTANT] Dastur .venv (virtual muhit) ichida ishlaydi. Shuning uchun kompyuteringizga qo'shimcha kutubxonalarni pip install orqali yuklab olishingiz shart emas — barcha kerakli resurslar paket ichida mavjud.

📝 Namuna (Tezkor kod)
Engine ichida o'z skriptingizni yozish uchun:

Python

from xns_engine import XNSApp

app = XNSApp()
# O'yin ob'ektlarini shu yerda yarating
app.run()
