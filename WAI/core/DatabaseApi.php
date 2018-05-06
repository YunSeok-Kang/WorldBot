<?php

class Database
{
	protected $dbConnection = NULL;
	public $selectedDB = NULL;

	function __construct($hostName, $userName, $userPw, $dbName) 
	{
		$this->db_connect($hostName, $userName, $userPw, $dbName);
	}
	
	function __destruct()
	{
		$this->db_close();
	}
	
	function db_connect($hostName, $userName, $userPw, $dbName)
	{
		$this->dbConnection = mysql_connect($hostName, $userName, $userPw);
		if (!$this->dbConnection)
		{
			echo 'connection failed!';
			return false;
		}
		
		$result = mysql_select_db($dbName, $this->dbConnection);
		
		return $this->select_db($dbName);
	}

	function select_db($dbName)
	{
		$this->selectedDB = mysql_select_db($dbName, $this->dbConnection);
		if(!$this->selectedDB)
		{
			echo 'DB Selection Failed!';
			return NULL;
		}
		
		return $this->selectedDB;
	}
	
	function db_close()
	{
		$this->mysqli_close($this->dbConnection);
	}
	
	// 쿼리문을 받아들인 후, 어떠한 타입의 명령인지 인지하여 그에 맞는 값을 자동으로 반환하게 수정하자.
	function query($queryStr)
	{
		$result = mysql_query($queryStr, $this->dbConnection) or die('쿼리문을 확인하세요');
		//while ($row = mysql_fetch_array($result))
			//echo $row['name'];
		
		return $result;
	}
}



?>