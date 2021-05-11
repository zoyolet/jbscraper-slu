import React from 'react';
import { Link } from 'react-router-dom';
import firebase from 'firebase/app';

export default function Menu() {

    const handleSignOut = () => {
        firebase.auth().signOut();
    }

    return (
        <aside>
            <ul>
                <li>
                    <Link to="/home">New Search</Link>
                </li>
                {/* <li>
                    <Link to="/dashboard">Dashboard</Link>
                </li> */}
                <li>
                    <Link onClick={handleSignOut} to="/login">Sign Out</Link>
                </li>
            </ul>
        </aside>
    )
}
