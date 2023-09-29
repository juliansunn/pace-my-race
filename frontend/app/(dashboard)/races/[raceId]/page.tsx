'use client';

import React from 'react';
import Loading from '../../../../components/Loading';
import { fetchRace } from '../../../../queries/races';
import { useQuery } from 'react-query';

export const revalidate = 60;

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
				<div
					className={`bg-gradient-to-l to-indigo-100 from-zinc-400 dark:from-zinc-500 h-72 mt-10 flex flex-row justify-start w-full relative`}
				>
					<img
						src={`${race.image}`}
						className="h-full w-full object-cover  mix-blend-overlay "
						alt="No Photo"
					/>
					<div className=" flex items-center gap-x-2 p-5 relative">
						<div className="w-1/2">
							<h1 className="text-2xl md:text-4xl  font-bold text-zinc-900 dark:text-zinc-200 drop-shadow-lg truncate pb-5">
								{race.name}
							</h1>
							<>
								<div className="flex flex-row space-x-2 text-zinc-800 dark:text-zinc-200">
									<h1>{race.name}</h1>
									<p className="whitespace-nowrap">
										{race.participant_count} Participants
									</p>
									{race.registration_open ? (
										<p className="whitespace-nowrap">Registration Open</p>
									) : (
										<p className="whitespace-nowrap">Registration Closed</p>
									)}
									<p className="whitespace-nowrap">
										Starts At: {formatDateTime(race.race_start)}
									</p>
								</div>
								{race.description && (
									<p className="text-sm text-zinc-700 dark:text-zinc-200 tracking-widest font-semibold flex-wrap">
										Description: {race.description}
									</p>
								)}
							</>
						</div>
					</div>
				</div>
			)}
		</>
	);
};

export default RaceDetails;
