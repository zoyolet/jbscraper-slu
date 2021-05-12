// https://www.youtube.com/watch?v=QFPSIT3ZR7Q - search bar
// https://www.youtube.com/watch?v=mZvKPtH9Fzo&t=2s - drop down & autocomplete search
import {useState} from 'react';
import firebase from 'firebase'
import JSONDATA from './searchLocations.json'
import './SearchBar.css'

export default function SearchBar({history}) {
    const [searchTerm, setSearchTerm] = useState("");
    const pricedata = [["property", "price"]]
    const ratingdata = [["property", "rating"]]
    const pricerating = [["price", "rating"]]

    const checkValid = () => {
        if (searchTerm === "") {
            alert ("invalid location")
        } 
        else if (['austin', 'chicago', 'st. louis'].includes(searchTerm.toLowerCase())) {
            const validLoc = searchTerm
            searchLocation()
            history.push({pathname:'/dash', state:{pricedata, ratingdata, pricerating, validLoc}});
            console.log(`SearchBar.js has: ${pricedata} ${ratingdata} ${pricerating} ${validLoc}`);
        } 
        else {
            alert ("see list for valid locations.")
        }
    }

    const searchLocation = () => {
        setSearchTerm(searchTerm)
        const ref = firebase.database().ref('properties');

        ref.orderByChild("location").equalTo(searchTerm.toLowerCase()).on("value", 
        function(snapshot) {
            snapshot.forEach(function(childSnapshot) {
                let key = childSnapshot.key
                let price = childSnapshot.val().price
                let rating = childSnapshot.val().rating
                pricedata.push([key, price]);
                ratingdata.push([key, rating]);
                pricerating.push([price, rating]);
            })
        }
        );
    }

    return(
        <div className = "Search">
            <div className = "TitleSection">
                <h1>
                    JB Scraper
                </h1>
                <form>
                    <input type="text" onChange={(event) => setSearchTerm(event.target.value)} placeholder="Location"/>
                    <button type="submit" onClick={checkValid}>Search</button>
                    <div className = "textbox">
                        {JSONDATA.filter((val) => {
                            if (searchTerm === "") {
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
                    </div> 
                </form>
                
            </div>
        </div>
    );
}