import React from 'react';
import Chart from "react-google-charts";
import ReactDOM from 'react-dom';

const data = [
    ["City", "Price of Property"],
    ["st. louis", 80],
    ["st. louis", 75],
    ["st. louis", 87],
    ["st. louis", 89],
    ["st. louis", 70],
    ["st. louis", 64],
];

class PriceChart extends React.Component{
    render() {
        return (
            <div className = "pricechart">
                <Chart  width={'100%'} 
                        height={'400px'} 
                        data = {data}
                        chartType="Histogram" 
                        options = {{
                            title: "Average Prices",
                            legend: {position: 'none'},
                            hAxis: {textPosition: 'out', title: 'Price of Property'},
                            vAxis: {textPosition: 'out', title: 'Number of Properties'}
                        }}
                        rootProps={{'data-testid':'3'}}
                />
            </div>
        )
    }
}

export default PriceChart