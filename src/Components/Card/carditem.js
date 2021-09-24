import React from 'react';
import './cards.css';

function CardItem(props) {

    if(props.percent > 0){
        return (
            <>
                <li className='cards__item'>
                    <div className='cards__item__link'>
                        <div className='cards__item__info'>
                            <h5 className='cards__item__text'>{props.counter}. {props.text}</h5>
                            <p className='p_stock_price_down' style={{ color: 'green' }}>${ props.price } &nbsp; +{ props.percent }%</p>
                        </div>
                    </div>
                </li>
            </>
        );
    } else {
        return (
            <>
                <li className='cards__item'>
                    <div className='cards__item__link'>
                        <div className='cards__item__info'>
                            <h5 className='cards__item__text'>{props.counter}. {props.text}</h5>
                            <p className='p_stock_price_down' style={{ color: 'red' }}>${ props.price } &nbsp; { props.percent }%</p>
                        </div>
                    </div>
                </li>
            </>
        );
    }

}

export default CardItem;
