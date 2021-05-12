import React from 'react';
import Chart from "react-google-charts";

class PriceRatingScatter extends React.Component{
    render() {
        return (
            <div className = "priceratingscatter">
                <Chart  width={'600px'} 
                        height={'400px'} 
                        data = {this.props.data}
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