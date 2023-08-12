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
			className="p-4 border-black/5 flex items-center justify-between hover:shadow-md transition cursor-pointer"
		>
			<h2>{race.name}</h2>
			{/* <div className="flex items-center gap-x-4">
				<div className={cn('p-2 w-fit rounded-md', race.bgColor)}>
					<race.icon className={cn('w-8 h-8', race.color)} />
				</div>
				<div className="font-semibold">{race.label}</div>
			</div>
			<ArrowRight className="w-5 h-5" /> */}
		</Card>
	);
};

export default RaceCard;
