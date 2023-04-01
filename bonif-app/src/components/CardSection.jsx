import './CardSection.scss';
import coffeSpillUrl from '../assets/coffe_spilling.png';
import { ReactComponent as BlackCoffee } from '../assets/black-coffee.svg';

const CardSection = () => {
  return (
    <div className="card-section">
      <section className="before-card">
        <section className="text-section">
          <div className="title"> Scan the card and collect as many points as possible </div>
          <div className="suggestin">Don't miss out any offer!</div>
        </section>
        <img src={coffeSpillUrl} alt="Coffee spilling" className="coffee-spilling" />
      </section>
      <div className="points-card">
        <div className="top-half">
          <BlackCoffee className="black-coffee" />
        </div>
        <div className="bottom-half"></div>
      </div>
    </div>
  );
};

export default CardSection;
