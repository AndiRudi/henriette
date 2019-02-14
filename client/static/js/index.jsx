import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            thrust: 0
        }   
    }
   

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
        }).then(x => x.json().then(r => this.setState({ thrust: r.thrust})));
    }

    render() {
        return (
    
            <div>
                Thrust: {this.state.thrust}<br/>
           
                <button onClick={() => this.thrust(this.state.thrust+10)} >Increase</button>
                <button onClick={() => this.thrust(this.state.thrust-10)} >Decrease</button>
                <button onClick={() => this.thrust(0)} >Stop</button>
            
             </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));