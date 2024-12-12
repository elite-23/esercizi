import './Navaber.css'
import Link from './Link'

const x = 3;
const img = "vite";

const imgStyle={
    height: x< 10?"300px":"800px",
    borderRadius: "90px"
}


function Navbar(){
    <>
        <nav>{x > 100000? "sono in alto" : "sono in basso"}</nav>
        <img style={imgStyle}src={`/${img}.svg`}></img>
        <ul>
            <li><Link></Link></li>
            <li><Link></Link></li>
            <li><Link></Link></li>
            <li><Link></Link></li>
            <li><Link></Link></li>
        </ul>
    </>
}

export default Navbar