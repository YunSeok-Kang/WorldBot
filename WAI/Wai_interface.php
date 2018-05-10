<?php
/*
외부와 통신하여 서비스 정보를 넘겨주는 php.
현재는 이 페이지를 로딩하자마자 데이터를 넘겨주기만 한다.
기능이 추가되면 바꿀 예정.
*/

require_once('core/DatabaseApi.php');

// read only
class WorldApplicaionInfo
{
	private $dataBase = NULL;
	
	function __construct() 
	{
		// 현재는 하드코딩 되어있지만, 이후에는 DB 정보 등은 파일로 만들어서 파싱해오는 형식으로 하자. 그래야 보안 문제가 해결됨.
		$this->dataBase = new Database('127.0.0.1', 'user01', '#09a28sh0', 'world_applications_info');
	}	
	
	private function HasServiceName($name)
	{
		return $this->dataBase->query("SELECT * FROM address_table WHERE name='$name'");
	}
	
	private function HasServicePort($port)
	{
		return $this->dataBase->query("SELECT * FROM hosting_info_table WHERE port='$port'");
	}
	
	private function HasHostingServer($hosting_server_name)
	{
		return $this->dataBase->query("SELECT * FROM address_table WHERE name='$hosting_server_name'");
	}
	
	// return type: Json Array
	function GetServicesInfo()
	{
		$result = $this->dataBase->query('SELECT address_table.name, address_table.domain, address_table.hosting_server, hosting_info_table.ip, address_table.port
					FROM address_table, hosting_info_table
					WHERE address_table.hosting_server = hosting_info_table.hosting_server');
		// 이 아래 반복문을 함수에서 자체적으로 처리할 수 있게 만들어야 함.
		$sendingArr = array();
		while ($row = mysql_fetch_array($result))
		{
			$jsonArr = array('name'=>$row[0], 'domain'=>$row[1], 'hosting_server'=>$row[2], 'ip'=>$row[3], 'port'=>$row[4]);
			array_push($sendingArr, $jsonArr);
		}
		return json_encode($sendingArr);
	}
	
	function AddService($name, $domain, $hosting_server, $port)
	{
		$result_msg = '';
		$noError = TRUE;
		if ($this->HasServiceName($name))
		{
			$result_msg = "db에 해당 이름의 필드가 이미 존재합니다. name:".$name."<br>";
			$noError = FALSE;
		}
		
		if ($this->HasServicePort($port))
		{
			$result_msg = $result_msg."db에 해당 이름의 필드가 이미 존재합니다. port:".$port."<br>";
			$noError = FALSE;
		}
		
		if ($this->HasHostingServer($hosting_server))
		{
			$result_msg = $result_msg."존재하지 않는 호스팅 서버입니다. hosting_server:".$hosting_server."<br>";
			$noError = FALSE;
		}
		
		if ($noError)
		{
			$query_str1 = "INSERT INTO address_table(name, ";
			$query_str2 = "hosting_server, port) VALUES('$name', ";
			if ($domain != NULL)
			{
				$query_str1 = $query_str1."domain, ";
				$query_str2 = query_str2."'$domain', ";
			}
			
			$this->dataBase->query($query_str1.$query_str2."'$hosting_server', '$port')");
		}
		
		return false;
	}
}

?>

<?php

$wai = new WorldApplicaionInfo();

// To do when page loaded
$command = $_GET['command'];
switch ($command) 
{
	case 'info':
		echo $wai->GetServicesInfo();
		break;
	case 'add':
		AddService($_GET['name'], $_GET['domain'], $_GET['hosting_server'], $_GET['port']);
		break;
}



?>