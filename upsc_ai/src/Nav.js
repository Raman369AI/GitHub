function Nav(props) {
    return (
        <nav className="main-nav">
            <ul>
                <li>Home</li>
                <li>{props.name} Indian History</li>
                <li>Ancient Indian History</li>
                <li>Medieval Indian History</li>
            </ul>
        </nav>
    );
};

export default Nav;