function barHelper(container, prepped_data, data_map){
    Highcharts.chart(container, {
        chart: {
            type: 'bar'
        },
        title: {
            text: null
        },
        subtitle: {
            text: null
        },
        xAxis: {
            type: 'category',
            labels: {
                formatter: function () {
                   return data_map[this.value];
                },
            },
        },
        yAxis: {
            title: {
                text: 'Number of times resource was recommended'
            },
            allowDecimals: false
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
            }
        },
        tooltip: {
            backgroundColor: 'rgba(236, 240, 241, .85)',
            style: {
                color: '#3B4B5C',
            },
            useHTML: true,
            headerFormat: '',
            pointFormat:  '<h6><strong>{point.y} users</strong></h6><hr><p>{point.name}</p>',
            shared: true,
            shadow: false,
            borderColor: '#3B4B5C'
        },
        series: [
            {
                "name": "Number of users",
                "colorByPoint": true,
                "data": prepped_data
            }
        ]
    });
}

function stackedBarHelper(container, prepped_data, data_map){
    Highcharts.chart(container, {
        chart: {
            type: 'bar'
        },
        title: {
            text: null
        },
        subtitle: {
            text: null
        },
        xAxis: {
          labels: {
            enabled: false
          },
          tickWidth: 0
        },
        yAxis: {
            title: {
                text: 'Percent of users ending on result'
            },
            allowDecimals: false
        },
        legend: {
            enabled: true
        },
        plotOptions: {
            series: {
              stacking: 'percent',
              dataLabels: {
                enabled: true,
                format: '{y:,.0f}%',
                color: '#fff',
                style: {
                  textShadow: 'none',
                  opacity: .8,
                  fontWeight: 'bold'
                }
              }
            }
        },
        tooltip: {
            backgroundColor: 'rgba(236, 240, 241, .85)',
            style: {
                color: '#3B4B5C',
            },
            useHTML: true,
            headerFormat: '',
            pointFormat:  '<h6><strong>{point.y} users</strong></h6><hr><p>{point.name}</p>',
            shared: true,
            shadow: false,
            borderColor: '#3B4B5C'
        },
        series: prepped_data
    });
}
