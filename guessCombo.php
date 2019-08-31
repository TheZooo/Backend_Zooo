<?php
session_start();
if (!(empty($_POST["restarty"]))) { //Restart session. Wipe session array clean
    session_destroy();
    session_abort();
    $_POST["restarty"] = false;
    header("Location: guessCombo.php"); //Duct-taped code: Refresh a second time to make sure the next if statments trigger
} 
if (!(isset($_SESSION["check"]))) { //Checks if "check" in session is not defined
    $_SESSION["check"] = false;
}
if (!(isset($_SESSION["correctStatus"]))) { 
    $_SESSION["correctStatus"] = 0;
}
if (!(isset($_SESSION["tries"]))) { 
    $_SESSION["tries"] = 0;
}
?>
<html>
    <head>
        <script>
            <?php
                $_SESSION["comboAmt"] = 4; //Changeable combination amount 
                $_SESSION["maxNum"] = 9; //Changeable number range of options
                if ($_SESSION["check"] == false) { //Generate four random numbers this session
                    for ($i = 0; $i < $_SESSION["comboAmt"]; $i++) {
                        $_SESSION["setNum".$i] = rand(0, $_SESSION["maxNum"]);
                    }
                    $_SESSION["check"] = true;
                }
            ?>
            var comboAmt = <?php echo $_SESSION['comboAmt'];?>; //Setting php variables as JS variables
            var maxNum = <?php echo $_SESSION['maxNum'];?>;
            var status = <?php echo $_SESSION['correctStatus'];?>;
            var tryCounter = <?php echo $_SESSION['tries'];?>;
            function start() {
                for (var i = 0; i < comboAmt; i++) { //Make select and options with the specified variables in the first form 'fofofo'
                    var sel = document.createElement('select');
                    var nam = document.createAttribute('name');
                    nam.value = "num" + i;
                    sel.setAttributeNode(nam);
                    for (var ii = 0; ii <= maxNum; ii++) {
                        var opt = document.createElement('option');
                        var num = document.createTextNode(ii);
                        var val = document.createAttribute('value');
                        val.value = ii;
                        opt.appendChild(num);
                        opt.setAttributeNode(val);
                        sel.appendChild(opt);
                    }
                    document.getElementById('fofofo').appendChild(sel); //Appending select element to first form 'fofofo'
                }
                trigger();
            }
            function trigger() {
                if (<?php echo boolval(isset($_SESSION["correctStatus"])) ?>) { //Checks if "correctStatus" is currently a set integer and returns as a boolean in JS
                    if (Number(status) == comboAmt) {
                        document.getElementById('feedback').innerHTML = "You guessed the combination!" <?php
                            if ($_SESSION['correctStatus'] === $_SESSION['comboAmt']) {
                                echo '+ " - " + "'.$_SESSION["setNum0"].$_SESSION["setNum1"].$_SESSION["setNum2"].$_SESSION["setNum3"].'"';
                            }
                            ?>; //Magical php that only shows if you guessed all the numbers
                    }
                    if (Number(status) < comboAmt) {
                        document.getElementById('feedback').innerHTML = status + " numbers are correct";
                    }
                }
                if (<?php echo boolval(isset($_SESSION["tries"])) ?>) {
                    document.getElementById('tried').innerHTML = "Guessed: " <?php echo '+'.$_SESSION["tries"] ?>;
                }
            }
        </script>
        <style>
            select {
                margin-left: 2px;
            }
            button {
                margin-left: 2px;
                margin-top: 2px;
            }
        </style>
    </head>
    <body onload="start()">
        <h3>Guess the combination</h3>
        <p>-Eric Zhou</p>
        <form id="fofofo" method="POST" action="guessComboCheck.php">
        <button id="submitBttn" type="submit">Check Numbers</button>
        </form>
        <form id="rerere" method="POST" action="guessCombo.php">
            <button id="resetBttn" type="submit" name="restarty" value="true">New Combo?</button>
        </form>
        <p id="feedback"></p>
        <p id="tried"></p>
    </body>
</html>
