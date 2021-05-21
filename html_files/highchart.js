Highcharts.chart('container', {
  chart: {
    renderTo: 'container' },

  title: {
    text: 'Test Results History'
  },


  yAxis: {
    title: {
      text: 'State'
    }
  },

  xAxis: {
    accessibility: {
      rangeDescription: 'Run Number'
    }
  },

  legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
  },

  plotOptions: {
    series: {
      label: {
        connectorAllowed: false
      },
      pointStart: 119
    }
  },

  series: [{
    name: 'Passed',
    data: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
  }, {
    name: 'Failed',
    data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  }, {
    name: 'Skipped',
    data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  }],

  responsive: {
    rules: [{
      condition: {
        maxWidth: 500
      },
      chartOptions: {
        legend: {
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom'
        }
      }
    }]
  }

});

Highcharts.chart('container2', {
  chart: {
    renderTo: 'container2' },

  title: {
    text: 'Coverage Results History'
  },


  yAxis: {
    title: {
      text: 'Coverage %'
    }
  },

  xAxis: {
    accessibility: {
      rangeDescription: 'Run Number'
    }
  },

  legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
  },

  plotOptions: {
    series: {
      label: {
        connectorAllowed: false
      },
      pointStart: 119
    }
  },

  series: [{
    name: '%',
    data: [18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87, 18.87]
  }],

  responsive: {
    rules: [{
      condition: {
        maxWidth: 500
      },
      chartOptions: {
        legend: {
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom'
        }
      }
    }]
  }
}
);