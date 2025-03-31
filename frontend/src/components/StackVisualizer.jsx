import React from 'react';

function StackVisualizer({ stack }) {
  return (
    <div>
      <h2>Stack:</h2>
      <ul>
        {stack.map((item, index) => (
          <li key={index}>{item}</li>
        )).reverse()}
      </ul>
    </div>
  );
}

export default StackVisualizer;
