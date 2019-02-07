'use strict';

const e = React.createElement;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
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
    }).then(x => x.json().then(r => console.debug(r)));
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.thrust(10) },
      'THRUST'
    );
  }
}

const domContainer = document.querySelector('#app');
ReactDOM.render(e(App), domContainer);