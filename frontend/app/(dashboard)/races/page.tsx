import React from 'react';
import { fetchRaces } from '../../../lib/api_functions';
import RaceCard from '../../../components/RaceCard';
import { NextResponse } from 'next/server';

type Props = {};

export const revalidate = 3600;

export default async function Races(props: Props) {
	const races: RacesResponse | NextResponse = await fetchRaces();
	if (races instanceof NextResponse) {
		// Handle unauthorized case
		return <div>Unauthorized</div>;
	}

	return (
		<div>
			{races.results.map((race: Race) => (
				<RaceCard race={race} />
			))}
		</div>
	);
}
