import Quest from './Quest';
import './Carousel.scss';

const Carousel = ({ questData }) => {
  const quests = ['daily', 'weekly', 'monthly'];

  return (
    <div className="carousel">
      <div className="quests-container">
        {quests.map((q, i) => {
          return (
            <Quest
              key={i}
              container={`quest-container${i}`}
              title="title"
              desc="desc"
              number="number"
              points="points"
              data={questData.data}
            />
          );
        })}
        <div className="point1">.</div>
        <div className="point2">.</div>
        <div className="point3">.</div>
      </div>
    </div>
  );
};

export default Carousel;
