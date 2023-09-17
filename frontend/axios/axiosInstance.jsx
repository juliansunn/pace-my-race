'use client';
import axios from 'axios';
import { useAuth } from '@clerk/nextjs';
import { useEffect } from 'react';

const axiosInstance = axios.create({
	baseURL: `${process.env.NEXT_PUBLIC_API_HOST}/api`
});

const AxiosInterceptor = ({ children }) => {
	const { getToken } = useAuth();

	useEffect(() => {
		const responseInterceptor = (response) => response;
		const errorInterceptor = (error) => Promise.reject(error);

		const interceptor = axiosInstance.interceptors.response.use(
			responseInterceptor,
			errorInterceptor
		);
		axiosInstance.interceptors.request.use(
			async (config) => {
				const authToken = await getToken();
				config.headers['Authorization'] = `Bearer ${authToken}`;
				return config;
			},
			(error) => {
				return Promise.reject(error);
			}
		);

		return () => axiosInstance.interceptors.response.eject(interceptor);
	}, []);

	return children;
};

export { AxiosInterceptor };
export default axiosInstance;
