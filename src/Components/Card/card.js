import React from 'react';
import { List } from 'semantic-ui-react'
import './cards.css'

export const Card = ({ listOfStocks })=> {
  return (
    <>
      <div className='cards'>
        <div className='cards__container'>
          <div className='cards__wrapper'>

            // <List className='cards__item'>
              {listOfStocks.map(stocks => (<li className='cards__item'>{stocks}</li>))}
            // </List>

          </div>
        </div>
      </div>
    </>
  )
}
