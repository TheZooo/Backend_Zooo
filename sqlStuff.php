<?php
$servername = "localhost";
$username = "erizho21";
$password = "zhou";
$dbname = "erizho21";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// sql to delete a record
//$sql = "DELETE FROM students WHERE id=2";

//if ($conn->query($sql) === TRUE) {
//    echo "Record deleted successfully";
//} else {
//    echo "Error deleting record: " . $conn->error;
//}
// Show Data
$sql = "SELECT * FROM students";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> id: " . $row["id"]. " - Name: " . $row["name"]. " " . $row["age"]. " - Grade: ". $row["gradeLevel"]. "<br>-<br>";
    }
} else {
    echo "0 results";
}

$conn->close();
?> 