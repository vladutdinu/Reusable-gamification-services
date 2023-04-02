import { useState } from 'react';
import Header from '../components/Header';
import useAxiosGet from '../helpers/useAxiosGet';
import './Coupons.scss';
import axios from 'axios';

const Coupons = () => {
  const [showList, setShowList] = useState('left');
  const customerPoints = useAxiosGet('http://localhost:8002/customer/points/1');
  const allcoupons = useAxiosGet('http://localhost:8002/coupon/all/1');
  const active = [];
  allcoupons?.data?.forEach((coupon) => {
    if (coupon.active) active.push(coupon);
  });

  const changeStatusCoupon = async (e) => {
    if (e.target.classList.contains('activate')) {
      e.target.classList.remove('activate');
      e.target.classList.add('activated');
      e.target.textContent = 'Activated';
      try {
        const response = await axios.put(
          `http://localhost:8002/coupon/activate/?coupon_id=${e.target.id}&customer_id=${e.target.dataset.id}`,
          { active: 1 }
        );
      } catch (err) {
        console.error(err);
      }
    } else {
      e.target.classList.add('activate');
      e.target.classList.remove('activated');
      e.target.textContent = 'Activate';
      try {
        console.log(`${e.target.id}/${e.target.dataset.id}`);
        const response = await axios.put(
          `http://localhost:8002/coupon/activate/?coupon_id=${e.target.id}&customer_id=${e.target.dataset.id}`,
          { active: 0 }
        );
      } catch (err) {
        console.error(err);
      }
    }
  };

  const showLeft = () => {
    setShowList('left');
  };
  const showRight = () => {
    setShowList('right');
  };

  return (
    <div className="coupons-page">
      <Header />
      <div className="coupon-header">
        <h1>Coupons</h1>
        <p className="points"> You have {customerPoints?.data?.points} points available </p>
      </div>
      <div className="switcher">
        <div className="all-coupons" onClick={showLeft}>
          All ({allcoupons?.data?.length})
        </div>
        <div className="active-coupons" onClick={showRight}>
          Active ({active.length})
        </div>
      </div>
      <div className={`bar-show-${showList}`}></div>
      <div className="list-coupons">
        {showList === 'left'
          ? allcoupons?.data?.map((coupon, i) => {
              return (
                <div key={i} className="coupon">
                  <div className="top-side">
                    <div className="title">{coupon.description}</div>
                    <div className="cost-points">Cost: {coupon.points_required} points </div>
                    <div className="available">
                      Available: {coupon.start_date.substring(8, 10)}.{coupon.start_date.substring(5, 7)} -{' '}
                      {coupon.end_date.substring(8, 10)}.{coupon.end_date.substring(5, 7)}.{coupon.end_date.substring(0, 4)}
                    </div>
                  </div>
                  {coupon.active === 1 ? (
                    <div className="activated" id={coupon.id} data-id={coupon.customer_id} onClick={changeStatusCoupon}>
                      Activated
                    </div>
                  ) : (
                    <div className="activate" id={coupon.id} data-id={coupon.customer_id} onClick={changeStatusCoupon}>
                      Activate
                    </div>
                  )}
                </div>
              );
            })
          : ''}
      </div>
    </div>
  );
};

const cop = {
  id: 1,
  points_required: 100,
  customer_id: 1,
  product_id: 1,
  description: 'Get discount on your next coffe',
  discount: 10,
  code: 'CODE1',
  start_date: '2023-04-01',
  end_date: '2023-04-05',
  done: 0,
  active: 0
};

export default Coupons;
