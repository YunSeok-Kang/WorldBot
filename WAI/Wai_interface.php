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
		$this->dataBase = new Database('ip 입력', '유저 이름', '비밀번호', '테이블');
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
}

?>

<?php
// To do when page loaded

$wai = new WorldApplicaionInfo();
echo $wai->GetServicesInfo();
?>