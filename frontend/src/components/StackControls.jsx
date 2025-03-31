import React, { useState } from 'react';

function StackControls({ onPush, onPop }) {
  const [input, setInput] = useState('');

  return (
    <div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter value"
      />
      <button onClick={() => {
        onPush(input);
        setInput('');
      }}>
        Push
      </button>
      <button onClick={onPop}>Pop</button>
    </div>
  );
}

export default StackControls;
