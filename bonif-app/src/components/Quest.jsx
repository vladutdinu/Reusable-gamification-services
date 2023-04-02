import React from 'react';
import './Quest.scss';

export default function Quest({ container, title, desc, number, points, data }) {
  return (
    <section className={container}>
      <div className={title}> {data?.type} </div>
      <div className={desc}> {data?.quest} </div>
      <div className="numbers-container">
        <p className={number}>
          {data?.quantity}/{data?.target_quantity}
        </p>
        <p className={points}> {data?.points}p </p>
      </div>
    </section>
  );
}
