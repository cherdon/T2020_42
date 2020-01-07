window.onload = function () {

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,

        title:{
            text:"Spending Summary"
        },
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Spendings (SGD $)"
        },
        data: [{
            type: "bar",
            name: "Amount",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: [
                { y: 2000, label: "December" },
                { y: 1000, label: "November" },
                { y: 3000, label: "September" },
                { y: 500, label: "August" },
                { y: 1000, label: "July" },
                { y: 2000, label: "June" },
                { y: 800, label: "May" },
                { y: 1245, label: "April" },
                { y: 3214, label: "March" },
                { y: 1400, label: "February" },
                { y: 2600, label: "January" }
            ]
        }]
    });
    chart.render();

}