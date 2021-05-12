import React from "react";
import Dashboard from './Dashboard/Dashboard';
import SearchBar from './Search/SearchBar';
import { Route, Switch } from "react-router-dom";

const Routes = () => (
    <Switch>
        <Route path="/search" exact component={SearchBar}/>
        <Route path="/dash" exact component={Dashboard}/>
    </Switch>
);

export default Routes;