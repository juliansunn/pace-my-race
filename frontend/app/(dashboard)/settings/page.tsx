'use client';

import React from 'react';
import { Card } from '@tremor/react';
import { ArrowRight, Compass, Settings, User } from 'lucide-react';
import { cn } from '../../../lib/utils';
import { useRouter } from 'next/navigation';
type Props = {};

const tools = [
	{
		label: 'General Settings',
		icon: Settings,
		href: '/general',
		color: 'text-violet-500',
		bgColor: 'bg-violet-500/10'
	},
	{
		label: 'Profile Settings',
		icon: User,
		href: '/user',
		color: 'text-emerald-500',
		bgColor: 'bg-emerald-500/10'
	},
	{
		label: 'Coach Settings',
		icon: Compass,
		href: '/coach',
		color: 'text-pink-700',
		bgColor: 'bg-pink-700/10'
	}
];

const SettingsNavigation = (props: Props) => {
	const router = useRouter();
	return (
		<div className="px-4 space-y-4">
			<h1 className="text-2xl font-bold">Settings</h1>
			{tools.map((tool) => (
				<Card
					onClick={() => router.push(`/settings/${tool.href}`)}
					key={tool.href}
					className="p-4 border-black/5 flex items-center justify-between hover:shadow-md transition cursor-pointer"
				>
					<div className="flex items-center gap-x-4">
						<div className={cn('p-2 w-fit rounded-md', tool.bgColor)}>
							<tool.icon className={cn('w-8 h-8', tool.color)} />
						</div>
						<div className="font-semibold">{tool.label}</div>
					</div>
					<ArrowRight className="w-5 h-5" />
				</Card>
			))}
		</div>
	);
};

export default SettingsNavigation;
