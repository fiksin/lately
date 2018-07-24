var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var svg = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// setup x 
var xScale = d3.scaleLinear().range([0, width]),
    xAxis = d3.axisBottom().scale(xScale),
    xValue = function(d) {return d.date};

// setup y
var yScale = d3.scaleLinear().range([height, 0]),
    yAxis = d3.axisLeft().scale(yScale),
    yValue = function(d) {return d.valence};



// x-axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
  .append("text")
    .attr("class", "label")
    .attr("x", width)
    .attr("y", -6)
    .style("text-anchor", "end")
    .text("Maturity");

// y-axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
  .append("text")
    .attr("class", "label")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Volatility");

// get data from csv
d3.csv("static/trackdata.csv", function(d) { // d is a common d3 variable for the data
    return {
        id: +d["id"],
        song: d["song"],
        artist: d["artist"],
        album: d["album"],
        date: d["date"].time.format("%Y-%m-%d"),
        danceability: +d["danceability"],
        energy: +d["energy"],
        key: +d["key"],
        loudness: +d["loudness"],
        mode: +d["mode"],
        speechiness: +d["speechiness"],
        acousticness: +d["acousticness"],
        instrumentalness: +d["instrumentalness"],
        liveness: +d["liveness"],
        valence: +d["valence"],
        tempo: +d["tempo"],
        timeSignature: +d["timeSignature"],
        genres: d["genres"],
        releaseDate: d["release date"],
        artistPop: +d["artist popularity"],
        trackPop: +d["track popularity"]
    };
});