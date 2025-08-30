import React from 'react';
import { Link, List } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import { Container, Box, ChakraProvider, HStack, VStack, defaultSystem, Card, Image , Heading, Highlight} from '@chakra-ui/react';
import image from './image.png';

function Nav() {
    return (
        <Container centerContent = 'true' fluid = 'true'>
        <nav>
            <ul style={{ display: 'flex', listStyleType: 'none', padding: 0, margin: 0 }}>
                <li style={{ marginRight: '10px' }}>
                    <Button variant="elevated" colorPalette = "#01352c" colorScheme = "teal">
                        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Home
                        </Link>
                    </Button>
                </li>
                <li>
                    <Button variant="elevated" colorPalette = "#01352c" colorScheme = "teal">
                        <Link to="/Modern-History" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Modern Indian History
                        </Link>
                    </Button>
                </li>
            </ul>
        </nav>
        </Container>
    );
}

export default Nav;
