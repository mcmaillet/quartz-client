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
      requestMessage: "Hello from the web app",
      responseMessage: ""
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleMessageChange = this.handleMessageChange.bind(this);
  }
  handleSubmit(selectedDate, requestMessage) {
    fetch('/api/createfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
           selectedDate: selectedDate,
           message: requestMessage
         }),
    }).then(response => {
        response.json()
            .then(x => {
                this.setState({ 
                  requestMessage: "",
                  responseMessage: x.message 
                })
            })
    });
  }
  handleDateChange(newDate) {
    this.setState({ selectedDate: newDate });
  }
  handleMessageChange(event){
    this.setState({ requestMessage: event.target.value });
  }
  render() {
  return (
    <div className="app-wrapper">
      <input type="text" value={this.state.requestMessage} onChange={this.handleMessageChange}/>
      <br />
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <DateTimePicker value={this.state.selectedDate} onChange={this.handleDateChange} />
    </MuiPickersUtilsProvider>
     <button onClick={() => this.handleSubmit(this.state.selectedDate, this.state.requestMessage)}>Submit</button>
     <div>{this.state.responseMessage}</div>
  </div>
  );
  }
}

export default App;
