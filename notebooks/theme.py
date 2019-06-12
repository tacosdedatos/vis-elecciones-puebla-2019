def cimarron_theme():
    markColor = "#282828"
    axisColor = "#282828"
    backgroundColor = "#FFFAFA"
    font = "Ubuntu"
    labelfont = "Ubuntu Condensed"
    sourcefont = "Ubuntu Mono"
    gridColor = "#C9C9C9"
    return {
        "width": 1080,
        "height": 800,
        "config": {
           "padding": 25,
           "geoshape": {
               "fill": "#C0C0C0",
               'stroke': '#C7C7C7',
               'strokeWidth': 0.3,
           },
           "arc": {
               "fill": markColor,
           },
           "area": {
               "fill": markColor,
           },
           "background": backgroundColor,
           "legend": {
               "labelFontSize": 18,
               "labelLimit": 500,
               "padding": 5,
               "symbolSize": 300,
               "symbolType": "square",
               "titleFontSize": 24,
               "titlePadding": 5,
               "titleLimit": 400,
           },
           "range": {
               "category": ["#F33C3C", "#1f62ae", "#683729", "#dc0d7a", "#02a3cd", "#e4a100", "#dc0d12", "#0DDC6F","#074a7e", "#e46800", "#aa3594", "#a20c4b"],
               "diverging": [
                   "#dc0d12",
                   "#e9686b",
                   "#fbe1e1",
                   "#dff4f9",
                   "#81d1e6",
                   "#03a3cd"
               ],
               "heatmap": [
                   "#fcdfef",
                   "#f8bfde",
                   "#f59fce",
                   "#f180be",
                   "#ee60ad",
                   "#eb409d",
                   "#e7208c",
                   "#e4007c",
               ],
           },
           "title":{
               "anchor": "start",
               "fontSize": 60,
               "fontWeight": 600,
               "offset": 20,
           },
           "view": {
               "stroke": 0,
               "padding": 10,
               
           },
       },
    }
    
    
import altair as alt
alt.themes.register("cimarron", cimarron_theme)
alt.themes.enable("cimarron")