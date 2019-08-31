<?php
    session_start();
    $_SESSION["correctStatus"] = 0; //Check if the random combo matches the user combo and increment the amt got correct
    for ($i = 0; $i < $_SESSION["comboAmt"]; $i++) {
        if ($_SESSION["setNum".$i] == $_POST["num".$i]) {
            $_SESSION["correctStatus"]++;
        }
    }
    if ($_SESSION["correctStatus"] !== $_SESSION["comboAmt"]) {
        $_SESSION["tries"]++;
    }
    echo "<script>";
    echo "location.href = 'guessCombo.php'";
    echo "</script>";
?>