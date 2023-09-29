import { AxiosResponse } from 'axios';
import axiosInstance from '../axios/axiosInstance';

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

export const unfavoriteRace = async (id: number): Promise<any> => {
	try {
		const response: AxiosResponse<any> = await axiosInstance.post(
			`/races/${id}/unfavorite/`
		);
		return response.data;
	} catch (error) {
		throw error;
	}
};
export const favoriteRace = async (id: number): Promise<any> => {
	try {
		const response: AxiosResponse<any> = await axiosInstance.post(
			`/races/${id}/favorite/`
		);
		return response.data;
	} catch (error) {
		throw error;
	}
};
