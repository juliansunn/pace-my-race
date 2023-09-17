import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { ClerkProvider } from '@clerk/nextjs';
import Background from '../components/theme/Background';
import { ThemeProvider } from '../components/theme/ThemeContext';

import './globals.css';
import Providers from './utils/provider';
import { AxiosInterceptor } from '../axios/axiosInstance';

const font = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
	title: 'Pace My Race',
	description: 'Run with a Pacer'
};

export default async function RootLayout({
	children
}: {
	children: React.ReactNode;
}) {
	return (
		<ThemeProvider initialTheme={null}>
			<ClerkProvider>
				<html lang="en" suppressHydrationWarning>
					<Background>
						<Providers>
							<body className={font.className}>
								<AxiosInterceptor>{children}</AxiosInterceptor>
							</body>
						</Providers>
					</Background>
				</html>
			</ClerkProvider>
		</ThemeProvider>
	);
}
