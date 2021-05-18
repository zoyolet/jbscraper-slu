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
        else if (['Texas', 'Illinois', 'Missouri'].includes(searchTerm)) {
            searchLocation(searchTerm);
        } 
        else {
            alert ("see list for valid locations.")
        }
    }

    // change the search term: search for state ("Missouri") in "location" field, instead.
    const searchLocation = () => {
        setSearchTerm(searchTerm)
        const ref = firebase.database().ref('properties');
        console.log(`search term is ${searchTerm}`)

        ref.orderByChild("state").equalTo(searchTerm).on("value", 
        function(snapshot) {
            snapshot.forEach(function(childSnapshot) {
                let key = childSnapshot.key
                let price = childSnapshot.val().price
                let rating = childSnapshot.val().rating
                pricedata.push([key, parseFloat(price)]);
                ratingdata.push([key, parseFloat(rating)]);
                pricerating.push([price, parseFloat(rating)]);
            })
        });
        history.push({pathname:'/dash', state:{pricedata, ratingdata, pricerating}});
    }

    return(
        <div className = "Search">
            <div className = "TitleSection">
                <h1>
                    JB Scraper
                </h1>
                <form>
                    <input type="text" onChange={(event) => setSearchTerm(event.target.value)} placeholder="Search a State"/>
                    <button type="submit" onClick={checkValid}>Search</button>
                    <div className = "textbox">
                        States currently available for search:
                        {JSONDATA.filter((val) => {
                            if (searchTerm === "") {
                                return val
                            }
                            else if (val.state.toLowerCase().includes(searchTerm.toLowerCase())) {
                                return val
                            }
                            else {
                                return ("No results found");
                            }
                        }).map((val, key) => {
                            return (
                                <div className="loc" key={key}>
                                    <p>-- {val.state}</p>
                                </div>
                            );
                        })}
                    </div> 
                </form>
                
            </div>
        </div>
    );
}