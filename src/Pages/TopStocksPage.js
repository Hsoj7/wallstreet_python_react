import React,{useState, useEffect} from 'react';
import { Card } from '../Components/Card/card';
import '../App.css'

export const TopStocksPage = ()=> {

  const [stocks, setStocks] = useState([]);
  const [prices, setPrices] = useState([]);
  const [percents, setPercents] = useState([]);
  let todaysDate = new Date();
  let number = todaysDate.getDate();
  let month = todaysDate.getMonth() + 1;

  let monthName = "";
  switch(month){
    case 1:
      monthName = monthName + "January";
      break;
    case 2:
      monthName = monthName + "February";
      break;
    case 3:
      monthName = monthName + "March";
      break;
    case 4:
      monthName = monthName + "April";
      break;
    case 5:
      monthName = monthName + "May";
      break;
    case 6:
      monthName = monthName + "June";
      break;
    case 7:
      monthName = monthName + "July";
      break;
    case 8:
      monthName = monthName + "August";
      break;
    case 9:
      monthName = monthName + "September";
      break;
    case 10:
      monthName = monthName + "October";
      break;
    case 11:
      monthName = monthName + "November";
      break;
    case 12:
      monthName = monthName + "December";
      break;
    //do nothing
    default:
      monthName = monthName
      break;
  }

  useEffect(()=> {
    fetch('/getSymbols').then(response => {
      if(response.ok){
        // return response.json()
        return response.json()
      }
    // }).then(data => console.log(data))
    }).then(data => {
    setStocks(data);
    })
  },[]);

  useEffect(()=> {
    fetch('/getPrices').then(response => {
      if(response.ok){
        return response.json()
      }
    }).then(data => {
      console.log("/getPrices got: " + data);
      setPrices(data);
    })
  },[]);

  useEffect(()=> {
    fetch('/getPercentChange').then(response => {
      if(response.ok){
        return response.json()
      }
    }).then(data => {
      console.log("/getPercentChange got: " + data);
      setPercents(data);
    })
  },[]);

  return(
    <>
      <h1>WallStreetBets top stocks for {monthName} {number}</h1>
      <h2>Compare the most discussed stocks from r/wallstreetbets. </h2>
      <Card listOfStocks={stocks} listOfPrices={prices} listOfPercents={percents}/>
    </>
  )
}

// <Card listOfTodos={todo}/>
// <ul>
//   {todo.map(stocks => (<li>{stocks}</li>))}
// </ul>
