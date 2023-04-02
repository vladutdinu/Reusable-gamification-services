import useAxiosGet from '../helpers/useAxiosGet';
import './Leaderboards.scss';

const Leaderboards = () => {
  const players = useAxiosGet('http://localhost:8002/leaderboard/all/2023-04-03');
  console.log(players.data);
  const leaderboard = players?.data?.leaderboard_result.sort((a, b) => {
    return a.points > b.points;
  });
  return (
    <div className="leaderboard">
      <h3>Top 2 of March</h3>
      {leaderboard?.map((player) => {
        console.log(player);
        return (
          <div className="leaderboard-player">
            <div className="index"> {player.index}. </div>
            <div className="playerindex"> name{player.name}</div>
            <div className="points">{player.points}</div>
          </div>
        );
      })}
    </div>
  );
};

export default Leaderboards;
