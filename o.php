<?php
// Подключение к базе данных
$db_host = 'localhost';
$db_user = 'usersi_usr';
$db_password = 'csb56kfrFsbUxRHi';
$db_name = 'usersi';
$conn = new mysqli($db_host, $db_user, $db_password, $db_name);
if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}




// Обработка данных формы регистрации


// Запускаем сессию
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
    $email = $_POST["email"];
    
    $avatar = $_FILES["avatar"]["name"];

    $avatar_tmp = $_FILES["avatar"]["tmp_name"];
    $age = $_POST["age"];

    // Проверка, не занят ли уже выбранный username
    $check_query = "SELECT * FROM users WHERE username = '$username'";
    $check_result = $conn->query($check_query);
    if ($check_result->num_rows > 0) {
        echo '<script>alert("Данный username уже занят");</script>';
    } else {
        // Проверка, не занят ли уже выбранный email
        $check_email_query = "SELECT * FROM users WHERE email = '$email'";
        $check_email_result = $conn->query($check_email_query);
        if ($check_email_result->num_rows > 0) {
            echo '<script>alert("Данный email уже зарегистрирован");</script>';
        } else {
            // Проверка валидности email
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                echo '<script>alert("Неправильный формат email");</script>';
            } else {
                // Проверка типа файла
                $allowed_types = array("image/jpeg", "image/png", "image/gif");
                $file_info = getimagesize($avatar_tmp);
                $file_type = $file_info["mime"];
                if (!in_array($file_type, $allowed_types)) {
                    echo '<script>alert("Допустимы только файлы формата JPEG, PNG и GIF");</script>';
                } else {
                    // Загрузка аватара
                    $avatar_directory = "avatars/";
                    move_uploaded_file($avatar_tmp, $avatar_directory.$avatar);

                    // Вставка данных пользователя в таблицу users
                    $insert_query = "INSERT INTO users (username, password, email, avatar, AGE) VALUES ('$username', '$password', '$email', '$avatar', '$age')";
                    if ($conn->query($insert_query) === TRUE) {
                        // Создание сессии
                        $_SESSION["username"] = $username;
                        $_SESSION["avatar"] = $avatar;
                        $_SESSION["email"] = $email;
                        $_SESSION["age"] = $age;

                        // Отправка приветственного письма
                        $to = $email;
                        $subject = "Добро пожаловать!";
                        $message = "Дорогой $username,

Сердечно приветствуем тебя на нашем сайте! Мы искренне благодарны за твою регистрацию. Надеемся, что ты найдешь здесь много интересного и полезного. Не стесняйся обращаться к нам в случае вопросов или пожеланий.

С наилучшими пожеланиями,
Команда нашего сайта

";
                        $headers = "From: danil@kerchi.fun";

                        $mail_sent = mail($to, $subject, $message, $headers);

                        if ($mail_sent) {
                            echo '<script>alert("Регистрация прошла успешно. Проверьте свою почту для получения приветственного письма.");</script>';
                        } else {
                            echo '<script>alert("Ошибка при отправке письма.");</script>';
                        }
                        

                        // Переход в личный кабинет
                        header("Location: ..\dh.php");
                        exit();
                    } else {
                        echo '<script>alert("Ошибка: ' . $insert_query . '");</script>';
                    }
                }
            }
        }
    }
}
$conn->close();
?>
