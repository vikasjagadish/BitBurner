<?php
session_start();
include("connect.php"); // Database connection

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Validate against DB (you can also add role checking here if needed)
    $query = mysqli_query($conn, "SELECT * FROM users1 WHERE email='$email' AND password='$password'");

    if (mysqli_num_rows($query) == 1) {
        $_SESSION['email'] = $email;

        // Redirect to homepage after login
        header("Location: homepage.php");
        exit();
    } else {
        echo "<script>alert('Invalid credentials'); window.history.back();</script>";
    }
}
?>
