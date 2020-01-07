import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import Login from './login.js'

class App extends Component {
    render() {
        return (
            <div>
                <Login />
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'))