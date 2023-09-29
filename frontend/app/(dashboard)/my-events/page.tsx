'use client';

import React from 'react';
import { fetchPaginatedRaces } from '../../../queries/races';
import { useQuery } from 'react-query';
import StaffRoute from '../../../components/StaffRoute';
import Loading from '../../../components/Loading';
import RaceCard from '../../../components/RaceCard';

type Props = {};

const MyEvents = (props: Props) => {
	const {
		data: races,
		error,
		isLoading
	} = useQuery('my-favorited-races', () =>
		fetchPaginatedRaces({ is_favorite: true })
	);
	return (
		<StaffRoute>
			<div>
				<h1 className="text-3xl font-bold">Races</h1>
				{isLoading ? (
					<Loading />
				) : (
					<div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3  gap-4">
						{races?.results?.map((race: Race) => (
							<RaceCard key={race.id} race={race} />
						))}
					</div>
				)}
			</div>
		</StaffRoute>
	);
};

export default MyEvents;
