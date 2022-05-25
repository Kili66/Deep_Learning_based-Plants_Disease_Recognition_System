import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";




function Navbar() {
    return (
        
        <div className="nav-container" >
           <ul className="nav-menu">
             <li className="nav-item">
                <Link to="/" className="nav-link">Main page</Link>
            </li>
             <li className="nav-item"><Link to="/Apple" className="nav-link">Apple</Link></li>

          <li className="nav-item"><Link to="/Patato" className="nav-link">Patato</Link></li>
            <li className="nav-item"> <Link to="/Tomato" className="nav-link">Tomato</Link></li>
            <li className="nav-item"> <Link to="/Corn"className="nav-link">Corn</Link> </li>
           <li className="nav-item"><Link to="/Grape" className="nav-link">Grape</Link> </li>

        </ul>
        </div>
         
    );
}
export default Navbar;