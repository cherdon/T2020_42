window.onload = function () {
    var spendings = [ {label: "January", y: 2000}, {label: "February", y: 1000}, {label: "March", y: 500}, {label: "April", y: 800} ];
    var chart = new CanvasJS.Chart("chartContainer1", {
        zoomEnabled: true,
        panEnabled: true,
        animationEnabled: true,
        title:{
            text:"Spending Summary"
        },
        axisX:{
            title: "Months"
        },
        axisY:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Spendings (SGD $)"
        },
        data: [
            {
                type: "column",
                name: "Spending per Month",
                dataPoints: spendings
            }
        ]
    });

    chart.render();
}