import './PointsTracker.scss';

const PointsTracker = ({ data }) => {
  <div className="points-tracker-container">
    <p>You have {data?.points} points</p>
  </div>;
};

export default PointsTracker;
