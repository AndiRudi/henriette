import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {

    thrust(amount) {
        fetch('/thrust', {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            amount: amount
            })
        }).then(x => x.json().then(r => console.debug(r)));
    }

    render() {
        return (
            <button onClick={() => this.thrust(10)} >Thrust</button>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));