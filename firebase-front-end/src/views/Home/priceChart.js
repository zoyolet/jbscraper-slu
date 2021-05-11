import React from 'react';
import Chart from "react-google-charts";
import ReactDOM from 'react-dom';

class PriceChart extends React.Component{
    
    render() {
        return (
            <div className = "pricechart">
                <Chart  width={'100%'} 
                        height={'400px'} 
                        data = {this.props.data}
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