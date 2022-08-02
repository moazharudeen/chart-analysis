chart_dict = {
'column2d' : """
<div id="{6}">chart will show here</div>
    <script type="text/javascript">
    //STEP 2 - Chart Data
    var chartData = {0};

    //STEP 3 - Chart Configurations
    var {7} = flower_open
    type: 'column2d',
    renderAt: '{6}',
    width: '100%',
    height: '400',
    dataFormat: 'json',
    dataSource: flower_open
        // Chart Configuration
        "chart": flower_open
            "caption": "{1}",
            "subCaption": "{2}",
            "xAxisName": "{3}",
            "yAxisName": "{4}",
            "numberSuffix": "{5}",
            "theme": "fusion",
            flower_close,
        // Chart Data
        "data": chartData
        flower_close
    flower_close;
    FusionCharts.ready(function()flower_open
    var fusioncharts = new FusionCharts({7});
    fusioncharts.render();
    flower_close);

</script>

"""
}