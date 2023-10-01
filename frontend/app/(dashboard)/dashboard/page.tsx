'use client';

import { useRouter } from 'next/navigation';

import RecommendedRaces from '../../../components/RecommendedRaces';

export default function HomePage() {
	const router = useRouter();

	return (
		<div>
			<div className="mb-8 space-y-4">
				<h2 className="text-2xl md:text-4xl font-bold text-center">
					Unlock Your True Potential
				</h2>
				<p className="text-muted-foreground font-light text-sm md:text-lg text-center">
					Find the perfect pacer to your next PR.
				</p>
			</div>
			<div className=" space-y-4">
				<RecommendedRaces />
			</div>
		</div>
	);
}
