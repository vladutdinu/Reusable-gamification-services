import './CardSection.scss';

const CardSection = () => {
  return (
    <div className="card-section">
      <div className="title"> Scan the card and collect as many points as possible </div>
      <div className="suggestin">Don't miss out any offer!</div>

      <div className="points-card">
        <div className="top-half"></div>
        <div className="bottom-half"></div>
      </div>
    </div>
  );
};

export default CardSection;
