
$(document).ready(function() {



google.charts.load('current', {'packages':['corechart']});



  google.charts.setOnLoadCallback(drawMaineChart);
    function drawMaineChart() {
      var data = google.visualization.arrayToDataTable([
        ['Year', 'Republican vote', 'Democrat vote'],
        ['2000 Bush(R) Gore(D)',  286616,                319951],
        ['2004 Bush(R) Kerry(D)',  330201,               396842],
        ['2008 McCain(R) Obama(D)',  295273,               421923],
        ['2012 Romney(R) Obama(D)',  292276,               401306],
        ['2016 Trump(R) Clinton(D)',  335593,               357735],
        ['2020 Trump(R) Biden(D)',  360737,               435072]
      ]);

      var options = {
        width: 800,
        colors:['red','blue'],
        legend: { position: 'bottom' },
        pointSize: 5
      };

      var chart = new google.visualization.LineChart(document.getElementById('test_chart'));

      chart.draw(data, options);
    }


})