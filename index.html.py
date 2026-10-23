<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой Mini App</title>
    <!-- Подключаем библиотеку Telegram Web Apps -->
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            /* Используем системные цвета Телеграма */
            background-color: var(--tg-theme-bg-color);
            color: var(--tg-theme-text-color);
            font-family: sans-serif;
            text-align: center;
            padding: 20px;
        }
        button {
            background-color: var(--tg-theme-button-color);
            color: var(--tg-theme-button-text-color);
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>Привет, это Mini App!</h1>
    <p id="user-info">Загрузка данных...</p>
    <button onclick="closeApp()">Закрыть приложение</button>

    <script>
        // Инициализация
        let tg = window.Telegram.WebApp;
        tg.expand(); // Разворачиваем на весь экран

        // Получаем данные пользователя, который открыл апп
        let user = tg.initDataUnsafe.user;
        if (user) {
            document.getElementById('user-info').innerText = 
                `Привет, ${user.first_name}! Твой ID: ${user.id}`;
        }

        function closeApp() {
            tg.close();
        }
    </script>
</body>
</html>
