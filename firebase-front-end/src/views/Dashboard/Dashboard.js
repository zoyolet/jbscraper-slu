import PriceChart from './priceChart'
import RatingChart from './ratingChart'
import PriceRatingScatter from './priceRatingScatter'
import './Dashboard.css'

export default function Dash(props) {
    const pricedata = props.location.state.pricedata
    const ratingdata = props.location.state.ratingdata
    const pricerating = props.location.state.pricerating
    const location = props.location.state.validLoc

    return(
        <div className = "dashbody">
            <div className = "header">
                <h1>
                    Showing data for location:  {location}
                </h1>
            </div>
            <div className = "charts">
                <PriceChart data={pricedata}/>
                <RatingChart data={ratingdata}/>
                <PriceRatingScatter data={pricerating}/>
            </div>              
        </div>
        
    );
}
