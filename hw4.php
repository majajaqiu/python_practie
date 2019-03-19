<?php
$DBNAME = "larry";
$DBUSER = "root";
$DBPASSWD = "";
$DBHOST = "localhost";
$student_id = (int)$_POST['student_id'];
$student_name = (string)$_POST['student_name'];
$conn = mysqli_connect( $DBHOST, $DBUSER, $DBPASSWD);
if (empty($conn)){
  print mysqli_error($conn);
  die ("無法連結資料庫");
  exit;
}
if( !mysqli_select_db($conn, $DBNAME)) {
  die ("無法選擇資料庫");
}
// 設定連線編碼
mysqli_query( $conn, "SET NAMES utf8");
$sql = " select *
		 from `student_info2`
		 where student_name = '$student_name' or student_id = $student_id";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
		echo "--------------------------------------------------------". "StandardAnswer". "---". 
				"BCCDEEDEABCDEEDAACDB"."<br>";
        echo "ID: " . $row["student_id"]. " - Name: " . $row["student_name"]. 
				" - Grade: " . $row["student_grade"]. " - student_range: ". $row["student_range"].
				" - Student Answer: ". $row["student_answer"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>

<form action="hw4.php" method="post">
student id:
<input type ="text" name="student_id" value="">
<input type ="submit" value="送出">
student name:
<input type ="text" name="student_name" value="">
<input type ="submit" value="送出">

</form>
