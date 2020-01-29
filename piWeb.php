<html>
	<head>
		<script>
			function switchLED(statusOfLED) {
				//A function that takes the parameter from button...
				//Sends the data to piLight.php
				var xmlhttp = new XMLHttpRequest();
				xmlhttp.open("GET", "piLight.php?turnOnOff=" + statusOfLED, true);
				xmlhttp.send();
				console.log("Function was triggered: " + statusOfLED);
			}
		</script>
	</head>
	<body>
		<button onclick="switchLED(0)">Turn LED On</button>
		<button onclick="switchLED(1)">Turn LED Off</button>
	</body>
</html>
