import PropTypes from 'prop-types';
import './Card.css'

function App({title, desc, imgUrl}) {

    return (
        <>
            <div>
                <h1>{title}</h1>
                <img src={imgUrl}/>
                <p>{desc}</p>

            </div>
        </>
  )
}

App.propTypes = {
    title: PropTypes.string.isRequired,
    desc: PropTypes.string.isRequired,
    imgUrl: PropTypes.string.isRequired
}

export default App