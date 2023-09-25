type User = {
	id: string;
	email: string;
	first_name: string;
	last_name: string;
	is_staff: boolean;
};

export const fetchUser = async (id: string, token: string): Promise<User> => {
	try {
		const url = `${process.env.NEXT_PUBLIC_API_HOST}/api/users/${id}`;
		const headers = {
			Authorization: `Bearer ${token}`
		};
		const response = await fetch(url, { headers });
		return response.json();
	} catch (error) {
		throw error;
	}
};
