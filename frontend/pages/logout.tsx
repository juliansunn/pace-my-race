import React, { useEffect } from 'react';
import { useAuth } from '../auth';
import Layout from '../components/Layout';

const Logout = () => {
	const { isAuthenticated, logout } = useAuth();

	useEffect(() => {
		logout();
	}, []);

	if (isAuthenticated) return null;
	return (
		<Layout>
			<h1 className="text-xl pt-3 pb-5">You have been logged out</h1>
		</Layout>
	);
};

export default Logout;
