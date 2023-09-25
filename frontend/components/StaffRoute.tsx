'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Cookies from 'js-cookie'; // Import the 'js-cookie' library
import Loading from './Loading';
import { useAuth } from '@clerk/nextjs';
import { fetchUser } from '../queries/users';

const StaffRoute = ({ children }) => {
	const router = useRouter();
	const [isLoading, setIsLoading] = useState(true);
	const { userId, getToken } = useAuth();

	useEffect(() => {
		const checkUser = async () => {
			const userDataCookie = Cookies.get('userData');
			let isStaff = false;
			if (userId && !userDataCookie) {
				const token = await getToken();
				const data = await fetchUser(userId, token || '');
				Cookies.set('userData', JSON.stringify(data));
				isStaff = data.is_staff;
			} else {
				const userData = JSON.parse(userDataCookie);
				isStaff = userData.is_staff;
			}
			if (!isStaff) {
				router.push('/dashboard');
			} else {
				setIsLoading(false);
			}
		};

		checkUser();
	}, [router]);

	if (isLoading) {
		return <Loading />;
	}

	return <>{children}</>;
};

export default StaffRoute;
