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
      pointStart: 2010
    }
  },

  series: [{
    name: 'Passed',
    data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
  }, {
    name: 'Failed',
    data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
  }, {
    name: 'Skipped',
    data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
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
      text: 'Total Coverage Functions'
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
      pointStart: 2010
    }
  },

  series: [{
    name: 'Passed',
    data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
  }, {
    name: 'Failed',
    data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
  }, {
    name: 'Skipped',
    data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
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