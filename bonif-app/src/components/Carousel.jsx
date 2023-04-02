import Quest from './Quest';
import './Carousel.scss';
import { useState } from 'react';

const Carousel = ({ questData }) => {
  const quests = ['daily', 'weekly', 'monthly'];
  const [shift, setShift] = useState(-23);

  const handleClickPoints = (e) => {
    const parentElement = e.target.parentNode;
    const childElement = parentElement.querySelector('.active');
    childElement && childElement.classList.contains('active') && childElement.classList.remove('active');

    e.target.classList.add('active');

    if (e.target.classList.contains('option1')) {
      return setShift(30);
    } else if (e.target.classList.contains('option2')) {
      return setShift(-23);
    } else {
      return setShift(-75);
    }
  };
  return (
    questData.data && (
      <div className="carousel">
        <div className="quests-container" style={{ transform: `translateX(${shift}%)` }}>
          {questData.data.map((q, i) => {
            return (
              <Quest
                key={i}
                container={`quest-container${i}`}
                title="title"
                desc="desc"
                number="number"
                points="points"
                data={q}
              />
            );
          })}
        </div>
        <div className="dots-container">
          <div onClick={handleClickPoints} className="option1"></div>
          <div onClick={handleClickPoints} className="option2 active"></div>
          <div onClick={handleClickPoints} className="option3"></div>
        </div>
      </div>
    )
  );
};

export default Carousel;
