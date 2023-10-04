'use client';

import React from 'react';
import Loading from '../../../../components/Loading';
import { fetchRace } from '../../../../queries/races';
import { useQuery } from 'react-query';
import {
	Tabs,
	TabsContent,
	TabsList,
	TabsTrigger
} from '../../../../components/ui/tabs';
import { Card, CardHeader, CardTitle } from '../../../../components/ui/card';

type Props = {
	params: { raceId: string };
};

const formatDateTime = (dateTime: Date) => {
	return dateTime.toLocaleString('en-US', { timeZone: 'America/New_York' });
};

const RaceDetails = ({ params: { raceId } }: Props) => {
	const {
		data: race,
		error,
		isLoading
	} = useQuery('race', () => fetchRace(raceId));
	return (
		<>
			{isLoading && <Loading />}
			{race && (
				<div className="p-2">
					<Card>
						<CardHeader>
							<CardTitle>{race.name}</CardTitle>
						</CardHeader>
					</Card>
					<Tabs defaultValue="details" className="w-full">
						<TabsList className="bg-inherit">
							<TabsTrigger className="" value="details">
								Race Details
							</TabsTrigger>
							<TabsTrigger className="" value="coaches">
								Coaches
							</TabsTrigger>
							<TabsTrigger className="" value="pacers">
								Pacers
							</TabsTrigger>
						</TabsList>
						<TabsContent value="details">details content here</TabsContent>
						<TabsContent value="coaches">Show Coach content here</TabsContent>
						<TabsContent value="pacers">Show Pacer content here</TabsContent>
					</Tabs>
				</div>
			)}
			{/* {race && (
				<div
					classNameName={`bg-gradient-to-l to-indigo-100 from-zinc-400 dark:from-zinc-500 h-72 mt-10 flex flex-row justify-start w-full relative`}
				>
					<Image
						src={`${race.image}`}
						height={24}
						width={24}
						classNameName="h-full w-full object-cover mix-blend-overlay"
						alt="No Photo"
					/>
					<div classNameName=" flex items-center gap-x-2 p-5 relative">
						<div classNameName="w-1/2">
							<h1 classNameName="text-2xl md:text-4xl  font-bold text-zinc-900 dark:text-zinc-200 drop-shadow-lg truncate pb-5">
								{race.name}
							</h1>
							<>
								<div classNameName="flex flex-row space-x-2 text-zinc-800 dark:text-zinc-200">
									<h1>{race.name}</h1>
									<p classNameName="whitespace-nowrap">
										{race.participant_count} Participants
									</p>
									{race.registration_open ? (
										<p classNameName="whitespace-nowrap">Registration Open</p>
									) : (
										<p classNameName="whitespace-nowrap">Registration Closed</p>
									)}
									<p classNameName="whitespace-nowrap">
										Starts At: {formatDateTime(race.race_start)}
									</p>
								</div>
								{race.description && (
									<p classNameName="text-sm text-zinc-700 dark:text-zinc-200 tracking-widest font-semibold flex-wrap">
										Description: {race.description}
									</p>
								)}
							</>
						</div>
					</div>
				</div>
			)} */}
		</>
	);
};

export default RaceDetails;
