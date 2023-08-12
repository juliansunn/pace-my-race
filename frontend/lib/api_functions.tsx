import { auth } from '@clerk/nextjs';
import { NextResponse } from 'next/server';

export function fullUrl(route: string) {
	return `${process.env.NEXT_PUBLIC_API_HOST}${route}`;
}

export const fetchRaces = async () => {
	const { userId, getToken } = auth();
	const url = fullUrl('/api/races');

	if (!userId) {
		return new NextResponse('Unauthorized', { status: 401 });
	}

	const authToken = `Bearer ${await getToken()}`;

	try {
		const response = await fetch(url, {
			headers: {
				'Content-Type': 'application/json',
				Authorization: authToken
			}
		});

		const racesData: RacesResponse = await response.json();
		return racesData; // Return the data retrieved from the fetch
	} catch (err) {
		console.error('[RACES ERROR]', err);
		throw err; // Re-throw the error to be caught by the caller if needed
	}
};
