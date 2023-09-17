'use-client';

import React from 'react';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import { Carousel } from 'react-responsive-carousel';

type Props = { children: any };

const RaceCarousel = ({ children }: Props) => {
	return <Carousel>{children}</Carousel>;
};

export default RaceCarousel;
