import React from 'react';
import { List } from 'semantic-ui-react'
import './cards.css'
import CardItem from './carditem'

export const Card = ({ listOfStocks, listOfPrices, listOfPercents})=> {
  var counter = 0;
  return (
    <>
      <div className='cards'>
        <div className='cards__container'>
          <div className='cards__wrapper'>

            {listOfStocks.map(stocks => {
              var price = listOfPrices[counter];
              var percent = listOfPercents[counter]
              counter++;
              return (
                <ul className='cards__items'><CardItem text={stocks} label='Stock' counter={counter} price={price} percent={percent}/></ul>
              );
            })}

          </div>
        </div>
      </div>
    </>
  )
}

// <ul className='cards__items'>
// <CardItem text='GOOG &nbsp;&nbsp; Alphabet Inc. - Class C Capital Stock' label='Stock'/>
// </ul>

// <ul className='cards__items'>
//   {listOfStocks.map(stocks => (<center><li className='cards__item'>{stocks}</li></center>))}
// </ul>

//FIGURE OUT WHATS GOING ON... ONLY PRINTING CHARS NOT IN COMMONENGLISH.TXT
