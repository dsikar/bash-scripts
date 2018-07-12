<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('/home/ubuntu/sqlite/buttons.db');
      }
   }
   $db = new MyDB();
   if(!$db) {
      echo $db->lastErrorMsg();
   } else {
      #echo "Opened database successfully\n";
	$json_output = "{";
	$result = $db->query('SELECT label, description FROM tblButtons');
	$i = 0;
	while($row = $result->fetchArray()) {
		# var_dump($row);	
		$json_output .= "\"" . $row['label'] . "\":\"" . $row['description'] . "\",";
	}
	$json_output = substr($json_output, 0, strlen($json_output)-1);
	$json_output .= "}";
	echo $json_output;
   }
?>
