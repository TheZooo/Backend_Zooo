<?php
session_start();
$_SESSION["check"] = false;
?>
<html>
    <head>
        <?php
            static $comboAmt = 4;
            static $maxNum = 9;

            if ($_SESSION["check"] == false) {
                for ($i = 0; $i < $comboAmt; $i++) {
                    $_SESSION["setNum".$i] = rand(0, $maxNum);
                }
                $_SESSION["check"] = true;
            }
        ?>
        <script>
            <?php
                echo "console.log(".$_SESSION["setNum0"]."+ ' ' +".$_SESSION["setNum1"]."+ ' ' +".$_SESSION["setNum2"]."+ ' ' +".$_SESSION["setNum3"].");";
            ?>

            var comboAmt = <?php echo $GLOBALS['comboAmt'];?>;
            var maxNum = <?php echo $GLOBALS['maxNum'];?>;
            
            function start() {
                for (var i = 0; i < comboAmt; i++) {
                    var sel = document.createElement('select');
                    for (var ii = 0; ii <= maxNum; ii++) {
                        var opt = document.createElement('option');
                        var num = document.createTextNode(ii);
                        var val = document.createAttribute('value');
                        val.value = ii;
                        opt.appendChild(num);
                        opt.setAttributeNode(val);
                        sel.appendChild(opt);
                    }
                    document.getElementsByTagName('div')[0].appendChild(sel);
                    
                }
            }
            function checker() {

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
        <div></div>
        <button onclick="checker()">Check</button>
    </body>
</html>