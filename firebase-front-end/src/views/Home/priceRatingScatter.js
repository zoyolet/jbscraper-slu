import React from 'react';
import Chart from "react-google-charts";
import ReactDOM from 'react-dom';

const data = [
    ["Price per Night", "Rating (out of 5)"],
    [80, 4.0],
    [75, 4.8],
    [87, 4.6],
    [89, 3.0],
    [70, 3.5],
    [64, 5.0],
];

class PriceRatingScatter extends React.Component{
    render() {
        return (
            <div className = "ratingchart">
                <Chart  width={'100%'} 
                        height={'400px'} 
                        data = {data}
                        chartType="ScatterChart" 
                        options = {{
                            title: "Price vs Rating Comparison",
                            hAxis: {title: 'Price per Night', minValue: 50, maxValue:150},
                            vAxis: {title: 'Rating', minValue:0, maxValue:5.01},
                            legend: 'none'
                        }}
                        rootProps={{'data-testid':'1'}}
                />
            </div>
        )
    }
}

export default PriceRatingScatter