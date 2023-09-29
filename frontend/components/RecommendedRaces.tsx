'use client';

import 'react-responsive-carousel/lib/styles/carousel.min.css'; // requires a loader

import React, { useState } from 'react';
import RaceCard from './RaceCard';
import { fetchPaginatedRaces } from '../queries/races';
import { useQuery } from 'react-query';

const RecommendedRaces = () => {
	const { data, error, isLoading } = useQuery('recommendedRaces', () =>
		fetchPaginatedRaces(1, 25)
	);
	const recommendedRaces = data?.results;

	return (
		<>
			{recommendedRaces &&
				recommendedRaces?.map((race: Race) => (
					<RaceCard key={race.id} race={race} />
				))}
		</>
	);
};

export default RecommendedRaces;
