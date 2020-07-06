// Word cloud 

d3.csv("NobelData/static/data/nobel.csv", function (data) {
    csvData = data;
    console.log('csvData:', data)
    var text = ''
    let motivations = csvData.map(function (d) {

        text += d.motivation.replace(/[""]+/g, '')
        // console.log('text:', text)
    })
    text = text.replace(/the\s+|which\s+|with\s+|its\s+|at\s+|th\s+|an\s+|orig\s+|as/g, '')
    text = text.replace(/of\s+|our\s+|use\s+|from\s+|new\s+|through\s+|they\s+|under\s+|which/g, '')
    text = text.replace(/in\s+|are\s+|her\s+|used\s+|how\s+|have\s+|more\s+|been\s+|CCC/g, '')
    text = text.replace(/his/g, '')
    text = text.replace(/and/g, '')
    text = text.replace(/ir\s+|to\s+|by\s+|he\s+|discoveries\s+|on\s+|for\s+|ory\s+|has/g, '')
    console.log('motivations:', motivations)
    console.log('text:', text)

    am4core.ready(function () {


        // Themes begin
        am4core.useTheme(am4themes_animated);
        // Themes end

        var chart = am4core.create("chartdiv2", am4plugins_wordCloud.WordCloud);
        var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

        series.accuracy = 4;
        series.step = 15;
        series.rotationThreshold = 0.7;
        series.maxCount = 150;
        series.minWordLength = 3;
        series.labels.template.margin(4, 4, 4, 4);
        series.maxFontSize = am4core.percent(30);

        series.text = text;
        series.colors = new am4core.ColorSet();
        series.colors.passOptions = {}; // makes it loop

        //series.labelsContainer.rotation = 45;
        series.angles = [0, -90];
        series.fontWeight = "700"

        setInterval(function () {
            series.dataItems.getIndex(Math.round(Math.random() * (series.dataItems.length - 1))).setValue("value", Math.round(Math.random() * 10));
        }, 20000)

        var title = chart.titles.create();
        title.text = "Top 150 words from Nobel Laureates motivations ";
        title.fontSize = 25;
        title.fill = '#ac434e';
        title.marginBottom = 60;
        title.marginTop = 40;

    }); // end am4core.ready()

}); // end of d3.csv("../static/data/nobel.csv", function (data) {