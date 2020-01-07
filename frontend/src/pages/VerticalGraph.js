window.onload = function () {
    var spendings = [ {label: "September 2019", y: 2507.90} , {label: "November 2019", y: 2712.65}, {label: "December 2019", y: 2651.90}, {label: "January 2020", y: 245.80} ];
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