'use client';

import React from 'react';
import { Card } from './ui/card';
import { useRouter } from 'next/navigation';
import { cn } from '../lib/utils';

type Props = {
	race: Race;
};

const RaceCard = ({ race }: Props) => {
	const router = useRouter();
	return (
		<Card
			onClick={() => router.push(`/races/${race.id}`)}
			key={race.id}
			className="p-4 border-black/2 flex items-center justify-between hover:shadow-md transition cursor-pointer"
		>
			<div className="flex-none mr-4">
				<img src={race.image} alt={race.name} className="w-16 h-16 rounded-full" />
			</div>

			<div className="flex flex-col justify-between">
				<h2 className="text-xl font-bold">{race.name}</h2>
				<div className="text-sm text-gray-600">
					{race.participants.length} Participants
				</div>
			</div>
		</Card>
	);
};

export default RaceCard;
