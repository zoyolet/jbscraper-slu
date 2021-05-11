// https://www.youtube.com/watch?v=QFPSIT3ZR7Q - search bar
// https://www.youtube.com/watch?v=mZvKPtH9Fzo&t=2s - drop down & autocomplete search
// https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/ - title case fucntion

import {useState} from 'react';
import firebase from 'firebase'
import JSONDATA from './searchLocations.json'

import PriceChart from './priceChart'
import RatingChart from './ratingChart'
import PriceRatingScatter from './priceRatingScatter'
{/* <priceChart></priceChart> */}

export default function Home() {
    const [searchTerm, setSearchTerm] = useState("");
    const [properties] = useState([]);
    
    //function to test if it is in the list
    const validLocation = () => {
        if (searchTerm == "") {
            alert ("invalid location")
        } 
        else if (['austin', 'chicago', 'st. louis'].includes(searchTerm)) {
            alert("valid")
        } 
        else {
            alert ("see list for valid locations.")
        }
    }

    const searchLocation = () => {
        setSearchTerm(searchTerm)
        validLocation()
        alert("Location searched is: " + searchTerm)
        const ref = firebase.database().ref('properties');

        ref.orderByChild("location").equalTo(searchTerm).on("value", 
        function(snapshot) {
            snapshot.forEach(function(childSnapshot) {
                let key = childSnapshot.key
                let price = childSnapshot.val().price
                let location = childSnapshot.val().location
                let rating = childSnapshot.val().rating
                alert(`property ${key} costs $ ${price}, is located in ${location} and rated ${rating}`);
            })
        }
        );
    }

    return(
        <div className = "Home">
            <div className = "TitleSection">
                <h1>
                    JB Scraper
                </h1>
                <input type="text" onChange={(event) => setSearchTerm(event.target.value)} placeholder="Location"/>
                {JSONDATA.filter((val) => {
                    if (searchTerm == "") {
                        return val
                    }
                    else if (val.city.toLowerCase().includes(searchTerm.toLowerCase())) {
                        return val
                    }
                    else {
                        return ("No results found");
                    }
                }).map((val, key) => {
                    return (
                        <div className="loc" key={key}>
                            <p>{val.city}</p>
                        </div>
                    );
                })}
                <button onClick={searchLocation}>Search</button>
            </div>
            <div className = "DisplaySection">
                <PriceChart/>
                <RatingChart/>
                <PriceRatingScatter/>
            </div>
        </div>
    );
}