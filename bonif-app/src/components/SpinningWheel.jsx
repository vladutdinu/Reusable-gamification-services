import Wheel from "rotatingwheel-kve3lq75zd"
import useAxiosGet from "../helpers/useAxiosGet"
export const SpinningWheel = () => {
   const slices = useAxiosGet("http://localhost:8000/spinningwheel/all/2023-04-03")
   
   return (
      <div className="spinning-container">
        <Wheel slices={slices} />
      </div>
   )
}