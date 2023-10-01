'use client';

import 'react-responsive-carousel/lib/styles/carousel.min.css'; // requires a loader

import React, { useState } from 'react';
import RaceCard from './RaceCard';
import { fetchPaginatedRaces } from '../queries/races';
import { useQuery } from 'react-query';
import Loading from './Loading';

const RecommendedRaces = () => {
	const { data, error, isLoading } = useQuery('recommended-races', () =>
		fetchPaginatedRaces({ page: 1, page_size: 25 })
	);
	const recommendedRaces = data?.results;

	return (
		<div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
			{isLoading ? (
				<Loading />
			) : (
				<>
					{recommendedRaces &&
						recommendedRaces?.map((race: Race) => (
							<RaceCard key={race.id} race={race} />
						))}
				</>
			)}
		</div>
	);
};

export default RecommendedRaces;
