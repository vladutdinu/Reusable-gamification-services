import { useState, useEffect } from "react";
import Wheel from "rotatingwheel-kve3lq75zd";
import useAxiosGet from "../helpers/useAxiosGet";
import axios from "axios";
import "./SpinningWheel.scss";
export const SpinningWheel = () => {
  const [slices, setSlices] = useState();
  const [finishedState, setFinishedState] = useState("");
  const [loading, setLoading] = useState(false)

//   useEffect(() => {
//    const fetchData = async () => {
//      setLoading(true)
//      try {
//        axios.get("http://localhost:8002/spinningwheel/all/2023-04-02").then(res => setSlices(res.data.slice.name))
//      } catch (err) {
//        console.log("err", err)
//      } finally {
//        setLoading(false);
//      }
     
//    };
//    fetchData();
//  }, []);
//   console.log(data);
//   setSlices(data.slice);
  if(loading){
   return <div>loading</div>
  }

  
  const segments = ["Try Again", "You won a coffee", "You won a latte", "You won a sandwich", "Free Coffee for a week", "Special Prize"];
  const slicesColors = [
    "#E05A45",
    "#BE9927",
    "#573512",
    "#586BA4",
    "#324376",
    "#58505B",
    "#584A49",
    "#584337",
  ];

  const onFinished = (winner) => {
    setFinishedState(winner);
  };

  return (
    <div className='spinning-container'>
          <Wheel
            slices={segments}
            slicesColors={slicesColors}
            primaryColor='#BE9927'
            contrastColor='#fff'
            buttonText='Spin'
            runOnlyOnce={true}
            size={200}
            upDuration={200}
            downDuration={1000}
            onFinished={onFinished}
            fontFamily='Roboto'
          />
    </div>
  );
};
