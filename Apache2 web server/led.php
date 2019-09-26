<html>
<head>
<title> LED CONTROL </title>
</head>
<body>
<h1 align= "center"> Control your LED </h1>
<form method = "post">
<table align="center">
<tr align="center">
<th align ="center"><input type="submit" name="00" value="0"></th>
<th align ="center"><input type="submit" name="01" value="1"></th>
<th align ="center"><input type="submit" name="10" value="2"></th>
<th align ="center"><input type="submit" name="11" value="3"></th>

</tr>
</table>
</form>



<?php
if(isset($_POST['00']))
{
system ('gpio write 4 0');
system ('gpio write 1 0');
}
if(isset($_POST['01']))
{
system ('gpio write 1 0');
system ('gpio write 4 1');
}
if(isset($_POST['10']))
{
system ('gpio write 1 1');
system ('gpio write 4 0');

}
if(isset($_POST['11']))
{
system ('gpio write 1 1');
system ('gpio write 4 1');
}
?>