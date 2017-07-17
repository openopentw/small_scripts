<?php
	exec("python interface.py", $out);
	/*
	for($i = 0; $i < count($out); $i ++) {
		echo $i.'<br>';
		echo $out[$i].'<br>';
	}
	 */
	$data = json_decode($out[0]);
	echo json_encode($data);
?>
