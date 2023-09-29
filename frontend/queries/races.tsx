// api.js
import { AxiosResponse } from 'axios';
import axiosInstance from '../axios/axiosInstance';

// Fetch paginated races
export const fetchPaginatedRaces = async (
	queryParams: any = {}
): Promise<RacesResponse> => {
	if (!queryParams.page) {
		queryParams.page = 1;
	}
	if (!queryParams.page_size) {
		queryParams.page_size = 10;
	}
	try {
		const response: AxiosResponse<RacesResponse> = await axiosInstance.get(
			'/races',
			{
				params: queryParams
			}
		);
		return response.data;
	} catch (error) {
		throw error;
	}
};
export const fetchMyFavoritedPaginatedRaces = async (
	page: number = 1,
	pageSize: number = 10
): Promise<RacesResponse> => {
	try {
		const response: AxiosResponse<RacesResponse> = await axiosInstance.get(
			'/races',
			{
				params: {
					page,
					page_size: pageSize
				}
			}
		);
		return response.data;
	} catch (error) {
		throw error;
	}
};

// fetch individual race
export const fetchRace = async (id: string): Promise<Race> => {
	try {
		const response: AxiosResponse<Race> = await axiosInstance.get(`/races/${id}`);
		return response.data;
	} catch (error) {
		throw error;
	}
};
