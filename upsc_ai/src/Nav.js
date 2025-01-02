import React from 'react';
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';

function Nav() {
    return (
        <nav className="main-nav">
            <ul style={{ display: 'flex', listStyleType: 'none', padding: 0, margin: 0 }}>
                <li style={{ marginRight: '10px' }}>
                    <Button variant="primary" class = "btn btn-primary">
                        <Link to="/" className="nav-item" style={{ color: 'white', textDecoration: 'none' }}>
                            Home
                        </Link>
                    </Button>
                </li>
                <li>
                    <Button variant="primary" class = "btn btn-primary">
                        <Link to="/Modern-History" className="nav-item" style={{ color: 'white', textDecoration: 'none' }}>
                            Modern Indian History
                        </Link>
                    </Button>
                </li>
            </ul>
        </nav>
    );
}

export default Nav;
