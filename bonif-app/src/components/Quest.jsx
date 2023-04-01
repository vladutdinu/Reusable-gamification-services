import React from 'react';
import './Quest.scss';

export default function Quest({ container, title, desc, number, points, data }) {
  return (
    <section className={container}>
      <p className={title}> {data.title} </p>
      <p className={desc}> {data.description} </p>
      <div>
        <p className={number}> {data.number} </p>
        <p className={points}> {data.points}p </p>
      </div>
    </section>
  );
}
