import React from 'react';

export const Card = ({ listOfTodos })=> {
  return (
    <>
      {listOfTodos.map(todo => {
        return(
          <ul key={todo.index}>
            <li>{todo.name}</li>
          </ul>
        )
      })}
      <p>This comes from card,js in components/ that is called from TodoPage.js in pages/ that is rendered in app.js</p>
    </>
  )
}
