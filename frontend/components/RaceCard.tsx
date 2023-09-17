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
			<h2>{race.name}</h2>
		</Card>
	);
};

export default RaceCard;
