<?php
//Recieve an XMLHTTP request from piWeb.php
$catch = $_REQUEST["turnOnOff"];
//Usual sql info
$servername = "";
$username = "piControl";
$password = "f103";
$dbname = "piLight";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//Updates the info in a database to switch on or off the LED
if ($catch == 0) {
    $sql = "UPDATE lightState SET switchLight='0'";
} else if ($catch == 1) {
    $sql = "UPDATE lightState SET switchLight='1'";
}
$result = $conn->query($sql);

//Close sql connection
$conn->close();
?>
