import React from 'react';
import './App.css';
import DateFnsUtils from '@date-io/date-fns';
import {
  DateTimePicker,
  MuiPickersUtilsProvider,
} from '@material-ui/pickers';

class App extends React.Component {
  constructor() {
    super();
    this.state = { 
      selectedDate: new Date(),
      message: ""
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleSubmit(selectedDate) {
    fetch('/api/createfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ selectedDate: selectedDate }),
    }).then(response => {
        response.json()
            .then(x => {
                this.setState({ message: x.message })
            })
    });
  }
  handleChange(newDate) {
    this.setState({ selectedDate: newDate });
  }
  render() {
  return (
    <div>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <DateTimePicker value={this.state.selectedDate} onChange={this.handleChange} />
    </MuiPickersUtilsProvider>
     <button onClick={() => this.handleSubmit(this.state.selectedDate)}>Submit</button>
     <div>{this.state.message}</div>
  </div>
  );
  }
}

export default App;
