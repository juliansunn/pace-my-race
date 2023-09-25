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
	const url =
		'https://utfs.io/f/c74de36c-811f-4981-94bb-c4edeb569071_Santa-Cruz-Beach-Boardwalk-2.jpg';
	return (
		<Card
			onClick={() => router.push(`/races/${race.id}`)}
			key={race.id}
			className="border-black/2 flex items-center hover:shadow-md transition cursor-pointer"
		>
			<div className="flex-none mr-4">
				<img src={url} alt={race.name} className="w-16 h-16 rounded-lg" />
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
