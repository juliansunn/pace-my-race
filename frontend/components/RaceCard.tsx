'use client';

import React from 'react';
import { Card } from './ui/card';
import { Heart } from 'lucide-react';
import Link from 'next/link';
import { favoriteRace, unfavoriteRace } from '../queries/users';
import { useMutation, useQueryClient } from 'react-query';

type Props = {
	race: Race;
};

const RaceCard = ({ race }: Props) => {
	const url =
		'https://utfs.io/f/c74de36c-811f-4981-94bb-c4edeb569071_Santa-Cruz-Beach-Boardwalk-2.jpg';

	const queryClient = useQueryClient();

	const favoriteMutation = useMutation((id: number) => favoriteRace(id), {
		onMutate: async (id: number) => {
			return id;
		},
		onSuccess: () => {
			queryClient.invalidateQueries('races');
			queryClient.invalidateQueries('my-favorited-races');
		}
	});

	const unfavoriteMutation = useMutation((id: number) => unfavoriteRace(id), {
		onMutate: async (id: number) => {
			return id;
		},
		onSuccess: () => {
			queryClient.invalidateQueries('races');
			queryClient.invalidateQueries('my-favorited-races');
		}
	});

	const toggleFavorite = () => {
		if (race.is_favorite) {
			unfavoriteMutation.mutate(race.id);
		} else {
			favoriteMutation.mutate(race.id);
		}
	};

	return (
		<Card
			key={race.id}
			className="border-black/2 flex hover:shadow-md transition"
		>
			<div className="flex-none mr-4">
				<img src={url} alt={race.name} className="w-24 h-24 rounded-l-lg" />
			</div>

			<div className="flex flex-col flex-grow mr-4 mt-2">
				<div className="flex flex-row justify-between">
					<Link
						href={`/races/${race.id}`}
						className="text-xl font-bold cursor-pointer transition 300 hover:text-[#FF80E5FF]"
					>
						{race.name}
					</Link>
					<Heart
						onClick={toggleFavorite}
						className="cursor-pointer"
						size={24}
						color="#FF80E5FF"
						fill={race.is_favorite ? '#FF80E5FF' : 'none'}
					/>
				</div>
				<div className="text-sm text-gray-600">
					{race.participant_count} Participants
				</div>
			</div>
		</Card>
	);
};

export default RaceCard;
