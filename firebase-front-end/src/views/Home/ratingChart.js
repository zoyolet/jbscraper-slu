import React from 'react';
import Chart from "react-google-charts";
import ReactDOM from 'react-dom';

const data = [
    ["City", "Rating (out of 5)"],
    ["st. louis", 4.0],
    ["st. louis", 4.8],
    ["st. louis", 4.6],
    ["st. louis", 3.0],
    ["st. louis", 3.5],
    ["st. louis", 5.0],
];

class RatingChart extends React.Component{
    render() {
        return (
            <div className = "ratingchart">
                <Chart  width={'100%'} 
                        height={'400px'} 
                        data = {data}
                        chartType="Histogram" 
                        options = {{
                            title: "Average Rating",
                            legend: {position: 'none'},
                            hAxis: {textPosition: 'out', title:'Rating, out of Five (*items in 5-6 bin are rating 5.0)', ticks: [0,1,2,3,4,5,6]},
                            vAxis: {textPosition: 'out', title:'Number of Properties'}
                        }}
                        rootProps={{'data-testid':'3'}}
                />
            </div>
        )
    }
}

export default RatingChart