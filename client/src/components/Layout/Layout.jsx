import { Outlet, Link } from 'react-router-dom';
import './Layout.css';

export default function Layout(){
    return (
        <div className='layout'>
            <nav className='navbar'>
                <Link to='/'>Home</Link>
                <Link to='/anime'>Anime</Link>
                <Link to='/characters'>Characters</Link>
            </nav>
            <Outlet />
            <footer className='footer'>
                FOOTER
            </footer>
        </div>
    );
}