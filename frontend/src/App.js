import React, { useState } from 'react';
import StackControls from './components/StackControls';
import StackVisualizer from './components/StackVisualizer';

function App() {
  const [stack, setStack] = useState([]);

  const handlePush = (value) => {
    setStack(prev => [...prev, value]);
  };

  const handlePop = () => {
    setStack(prev => prev.slice(0, -1));
  };

  return (
    <div>
      <h1>EzDSViewer</h1>
      <StackControls onPush={handlePush} onPop={handlePop} />
      <StackVisualizer stack={stack} />
    </div>
  );
}

export default App;
