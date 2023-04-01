import './App.scss';
import React from 'react';
import Quest from './components/Quest';
import Header from './components/Header';
import Welcome from './components/Welcome';
import CardSection from './components/CardSection';

function App() {
  const data = {};
  const quests = [];
  for (let i = 0; i <= 2; i++) {
    quests.push(i);
  }

  console.log(quests);
  return (
    <div className="App">
      <Header />
      <Welcome />
      <div className="quests-container">
        {quests.map((q) => {
          return (
            <Quest container={`quest-container${q}`} title="title" desc="desc" number="number" points="points" data={data} />
          );
        })}
      </div>
      <CardSection />
    </div>
  );
}

export default App;
