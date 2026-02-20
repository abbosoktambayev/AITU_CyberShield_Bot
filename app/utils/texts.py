TEXTS = {

    # ================= QUIZ ANSWERS =================
    "quiz_answer": {
        "correct": {
            "ru": "✅ Верно! Это правильный ответ.",
            "kz": "✅ Дұрыс! Бұл дұрыс жауап.",
            "uz": "✅ To‘g‘ri! Bu to‘g‘ri javob.",
            "en": "✅ Correct! This is the right answer.",
        },
        "wrong": {
            "ru": "❌ Неверно. Это неправильный вариант.",
            "kz": "❌ Қате. Бұл дұрыс емес жауап.",
            "uz": "❌ Noto‘g‘ri. Bu noto‘g‘ri javob.",
            "en": "❌ Wrong. This is the wrong option.",
        },
    },

    # ================= RUSSIAN =================
    "ru": {
        "start": "👋 Привет! Выберите язык:",
        "menu": "Главное меню. Выберите действие 👇",
        "ask_password": "Введите пароль для проверки:",
        "back": "🔙 Назад",
        "choose_option": "Выберите вариант:",
        "test_finished": "🏁 Тест завершён!\n\nРезультат: {score} / {total}",

        "btn_fake": "❌ Мошенники",
        "btn_real": "✅ Официально",
        "btn_next": "▶️ Следующий вопрос",
        "btn_menu": "⬅️ В меню",

        "quiz_questions": [
            {
                "text": "📩 SMS:\n\n«Ваша банковская карта заблокирована.\nСрочно перейдите по ссылке:\n👉 bank-secure.com»\n\nЧто это?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Обнаружена подозрительная активность.\nПодтвердите аккаунт, иначе он будет удалён»\n\nЧто это?",
                "correct": "fake",
            },
            {
                "text": "💬 Сообщение:\n\n«Здравствуйте! Я из службы поддержки.\nОтправьте код из SMS для подтверждения»\n\nЧто это?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Вы успешно вошли в аккаунт с нового устройства.\nЕсли это были вы — никаких действий не требуется»\n\nЧто это?",
                "correct": "real",
            },
            {
                "text": "📱 Уведомление банка:\n\n«Баланс обновлён. Посмотреть детали можно в приложении»\n\nЧто это?",
                "correct": "real",
            },
            {
                "text": "📧 Email:\n\n«Ваш чек по операции доступен в личном кабинете.\nСпасибо за использование сервиса»\n\nЧто это?",
                "correct": "real",
            },
        ],

        "sos_question": "Что случилось? Выберите ситуацию:",
        "sos_account": "🔓 Взломали аккаунт",
        "sos_money": "💳 Украли деньги",
        "sos_account_text": (
            "🔐 Если взломали аккаунт:\n\n"
            "1) Срочно смените пароль\n"
            "2) Включите 2FA\n"
            "3) Проверьте активные сессии\n"
            "4) Напишите в поддержку сервиса"
        ),
        "sos_money_text": (
            "💳 Если украли деньги:\n\n"
            "1) Немедленно заблокируйте карту\n"
            "2) Позвоните в банк\n"
            "3) Подайте заявление\n"
            "4) Не переходите по подозрительным ссылкам"
        ),
    },

    # ================= KAZAKH =================
    "kz": {
        "start": "👋 Сәлем! Тілді таңдаңыз:",
        "menu": "Басты мәзір. Таңдаңыз 👇",
        "ask_password": "Құпиясөзді енгізіңіз:",
        "back": "🔙 Артқа",
        "choose_option": "Нұсқаны таңдаңыз:",
        "test_finished": "🏁 Тест аяқталды!\n\nНәтиже: {score} / {total}",

        "btn_fake": "❌ Алаяқтар",
        "btn_real": "✅ Ресми",
        "btn_next": "▶️ Келесі сұрақ",
        "btn_menu": "⬅️ Мәзірге",

        "quiz_questions": [
            {
                "text": "📩 SMS:\n\n«Банк картаңыз бұғатталды.\nШұғыл түрде мына сілтемеге өтіңіз:\n👉 bank-secure.com»\n\nБұл не?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Күдікті әрекет анықталды.\nАккаунтты растаңыз, әйтпесе ол жойылады»\n\nБұл не?",
                "correct": "fake",
            },
            {
                "text": "💬 Хабарлама:\n\n«Сәлеметсіз бе! Бұл қолдау қызметі.\nSMS-тегі кодты жіберіңіз»\n\nБұл не?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Сіз аккаунтқа жаңа құрылғыдан кірдіңіз.\nЕгер бұл сіз болсаңыз — ештеңе істеудің қажеті жоқ»\n\nБұл не?",
                "correct": "real",
            },
            {
                "text": "📱 Банк қосымшасы:\n\n«Баланс жаңартылды. Толығырақ қосымшада»\n\nБұл не?",
                "correct": "real",
            },
            {
                "text": "📧 Email:\n\n«Операция чегі жеке кабинетте қолжетімді»\n\nБұл не?",
                "correct": "real",
            },
        ],

        "sos_question": "Не болды? Жағдайды таңдаңыз:",
        "sos_account": "🔓 Аккаунт бұзылды",
        "sos_money": "💳 Ақша ұрланды",
        "sos_account_text": (
            "🔐 Аккаунт бұзылса:\n\n"
            "1) Құпиясөзді ауыстырыңыз\n"
            "2) 2FA қосыңыз\n"
            "3) Белсенді сессияларды тексеріңіз\n"
            "4) Қолдау қызметіне жазыңыз"
        ),
        "sos_money_text": (
            "💳 Ақша ұрланса:\n\n"
            "1) Картаны дереу бұғаттаңыз\n"
            "2) Банкке қоңырау шалыңыз\n"
            "3) Өтініш жазыңыз\n"
            "4) Күмәнді сілтемелерге өтпеңіз"
        ),
    },

    # ================= UZ =================
    "uz": {
        "start": "👋 Salom! Tilni tanlang:",
        "menu": "Asosiy menyu. Tanlang 👇",
        "ask_password": "Parolni kiriting:",
        "back": "🔙 Orqaga",
        "choose_option": "Variantni tanlang:",
        "test_finished": "🏁 Test yakunlandi!\n\nNatija: {score} / {total}",

        "btn_fake": "❌ Firibgarlar",
        "btn_real": "✅ Rasmiy",
        "btn_next": "▶️ Keyingi savol",
        "btn_menu": "⬅️ Menyuga",

        "quiz_questions": [
            {
                "text": "📩 SMS:\n\n«Bank kartangiz bloklandi.\nZudlik bilan havolaga o‘ting:\n👉 bank-secure.com»\n\nBu nima?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Shubhali faollik aniqlandi.\nAkkountni tasdiqlang»\n\nBu nima?",
                "correct": "fake",
            },
            {
                "text": "💬 Xabar:\n\n«SMS kodni yuboring»\n\nBu nima?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n«Yangi qurilmadan kirish amalga oshirildi»\n\nBu nima?",
                "correct": "real",
            },
            {
                "text": "📱 Bank ilovasi:\n\n«Balans yangilandi»\n\nBu nima?",
                "correct": "real",
            },
            {
                "text": "📧 Email:\n\n«Operatsiya cheki mavjud»\n\nBu nima?",
                "correct": "real",
            },
        ],

        "sos_question": "Nima bo‘ldi? Vaziyatni tanlang:",
        "sos_account": "🔓 Akkount buzildi",
        "sos_money": "💳 Pul o‘g‘irlandi",
        "sos_account_text": (
            "🔐 Akkount buzilsa:\n\n"
            "1) Parolni almashtiring\n"
            "2) 2FA yoqing\n"
            "3) Sessiyalarni tekshiring\n"
            "4) Qo‘llab-quvvatlashga yozing"
        ),
        "sos_money_text": (
            "💳 Pul o‘g‘irlangan bo‘lsa:\n\n"
            "1) Kartani bloklang\n"
            "2) Bankka qo‘ng‘iroq qiling\n"
            "3) Ariza bering\n"
            "4) Shubhali havolalarga kirmang"
        ),
    },

    # ================= EN =================
    "en": {
        "start": "👋 Hello! Choose language:",
        "menu": "Main menu. Choose an action 👇",
        "ask_password": "Enter password:",
        "back": "🔙 Back",
        "choose_option": "Choose an option:",
        "test_finished": "🏁 Test finished!\n\nResult: {score} / {total}",

        "btn_fake": "❌ Scammers",
        "btn_real": "✅ Official",
        "btn_next": "▶️ Next question",
        "btn_menu": "⬅️ To menu",

        "quiz_questions": [
            {
                "text": "📩 SMS:\n\n“Your card is blocked.\nVisit: bank-secure.com”\n\nWhat is this?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n“Suspicious activity detected.\nConfirm your account”\n\nWhat is this?",
                "correct": "fake",
            },
            {
                "text": "💬 Message:\n\n“Send SMS code to verify”\n\nWhat is this?",
                "correct": "fake",
            },
            {
                "text": "📧 Email:\n\n“Login from a new device”\n\nWhat is this?",
                "correct": "real",
            },
            {
                "text": "📱 Bank app:\n\n“Balance updated”\n\nWhat is this?",
                "correct": "real",
            },
            {
                "text": "📧 Email:\n\n“Your receipt is available”\n\nWhat is this?",
                "correct": "real",
            },
        ],

        "sos_question": "What happened? Choose a situation:",
        "sos_account": "🔓 Account hacked",
        "sos_money": "💳 Money stolen",
        "sos_account_text": (
            "🔐 If your account was hacked:\n\n"
            "1) Change password\n"
            "2) Enable 2FA\n"
            "3) Check sessions\n"
            "4) Contact support"
        ),
        "sos_money_text": (
            "💳 If money was stolen:\n\n"
            "1) Freeze card\n"
            "2) Call bank\n"
            "3) File report\n"
            "4) Avoid suspicious links"
        ),
    },
}