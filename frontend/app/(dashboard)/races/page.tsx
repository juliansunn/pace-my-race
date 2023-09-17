'use client';

import React, { useState } from 'react';
import RaceCard from '../../../components/RaceCard';
import Loading from '../../../components/Loading';
import { useQuery } from 'react-query';
import { fetchPaginatedRaces } from '../../../queries/races';

type Props = {};

export const revalidate = 3600;

export default function Races(props: Props) {
	const {
		data: races,
		error,
		isLoading
	} = useQuery('races', () => fetchPaginatedRaces());
	console.log('races', races);

	return (
		<div>
			<h1 className="text-3xl font-bold">Races</h1>
			{isLoading ? (
				<Loading />
			) : (
				<div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
					{races?.results?.map((race: Race) => (
						<RaceCard key={race.id} race={race} />
					))}
				</div>
			)}
		</div>
	);
}
