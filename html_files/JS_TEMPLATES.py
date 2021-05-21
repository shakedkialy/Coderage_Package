HIGHCHARTS_MSG = """Highcharts.chart('container', {{
  chart: {{
    renderTo: 'container' }},

  title: {{
    text: 'Test Results History'
  }},


  yAxis: {{
    title: {{
      text: 'State'
    }}
  }},

  xAxis: {{
    accessibility: {{
      rangeDescription: 'Run Number'
    }}
  }},

  legend: {{
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
  }},

  plotOptions: {{
    series: {{
      label: {{
        connectorAllowed: false
      }},
      pointStart: {}
    }}
  }},

  series: [{{
    name: 'Passed',
    data: {}
  }}, {{
    name: 'Failed',
    data: {}
  }}, {{
    name: 'Skipped',
    data: {}
  }}],

  responsive: {{
    rules: [{{
      condition: {{
        maxWidth: 500
      }},
      chartOptions: {{
        legend: {{
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom'
        }}
      }}
    }}]
  }}

}});

Highcharts.chart('container2', {{
  chart: {{
    renderTo: 'container2' }},

  title: {{
    text: 'Coverage Results History'
  }},


  yAxis: {{
    title: {{
      text: 'Coverage %'
    }}
  }},

  xAxis: {{
    accessibility: {{
      rangeDescription: 'Run Number'
    }}
  }},

  legend: {{
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
  }},

  plotOptions: {{
    series: {{
      label: {{
        connectorAllowed: false
      }},
      pointStart: {}
    }}
  }},

  series: [{{
    name: '%',
    data: {}
  }}],

  responsive: {{
    rules: [{{
      condition: {{
        maxWidth: 500
      }},
      chartOptions: {{
        legend: {{
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom'
        }}
      }}
    }}]
  }}
}}
);"""


HIGHCHARTS2_MSG = """Highcharts.chart('container', {
  chart: {
    type: 'column'
  },
  title: {
    text: 'Stacked column chart'
  },
  xAxis: {
    categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
  },
  yAxis: {
    min: 0,
    title: {
      text: 'Total fruit consumption'
    }
  },
  tooltip: {
    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
    shared: true
  },
  plotOptions: {
    column: {
      stacking: 'percent'
    }
  },
  series: [{
    name: 'John',
    data: [5, 3, 4, 7, 2]
  }, {
    name: 'Jane',
    data: [2, 2, 3, 2, 1]
  }]
});"""