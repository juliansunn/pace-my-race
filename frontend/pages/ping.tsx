import React, { useState } from 'react';
import Layout from '../components/Layout';

const Ping = (): React.ReactElement => {
	const [awaitingResponse, setAwaitingResponse] = useState<boolean>(false);
	const [apiResponse, setAPIResponse] = useState<string>('');

	const handleClick = async () => {
		setAwaitingResponse(true);
		const url = process.env.NEXT_PUBLIC_API_HOST + '/ping/';
		const resp = await fetch(url, {
			method: 'GET',
			headers: {
				Authorization: `Bearer `
			}
		});
		if (resp.ok) {
			const data = await resp.json();
			setAPIResponse(data.now);
		} else {
			setAPIResponse('Error during API call');
		}
		setAwaitingResponse(false);
	};

	return (
		<Layout>
			<h1 className="text-xl pt-3 pb-5">Ping</h1>
			<p className="pb-4">
				This page demos the background refresh of the access token by pinging a
				protected API route.
			</p>
			<button
				className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
				onClick={handleClick}
				disabled={awaitingResponse}
			>
				{awaitingResponse ? 'Loading' : 'Click to ping API'}
			</button>
			<p className="py-4">Current time: {apiResponse}</p>
		</Layout>
	);
};

export default Ping;
