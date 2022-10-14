<?php
$connect = mysqli_connect("localhost", "root", "root", "electionproject")
$query = select State from 2020_election where id > 20
$result =  mysqli_query($connect, $query)
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type = "text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type = "text/javascript">
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart(){
            var data = google.visualization.arrayToDataTable([
            ['State'],
            <?php
            while($row = mysqli_fetch_array($result))
            {
                echo "['".$row["state"]."'],";
            }
            ?>
            ]);
        var options:{
            title:'Testing'
        };
        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
        }
    </script>
</head>
<body>
    <div style = "width:900px;">
        <div id = "piechart" style = "width:900px; height:500px">
        </div>
    </div>


</body>
</html>