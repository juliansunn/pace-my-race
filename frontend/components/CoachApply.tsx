'use client';

import Link from 'next/link';
import { zodResolver } from '@hookform/resolvers/zod';
import { useFieldArray, useForm } from 'react-hook-form';
import * as z from 'zod';

import { cn } from '../lib/utils';
import { Button } from './ui/button';
import {
	Form,
	FormControl,
	FormDescription,
	FormField,
	FormItem,
	FormLabel,
	FormMessage
} from './ui/form';
import { Input } from './ui/input';
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue
} from './ui/select';
import { Textarea } from './ui/textarea';
import { toast } from './ui/use-toast';
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle
} from './ui/card';
import { useAuth, useClerk } from '@clerk/nextjs';

const coachFormSchema = z.object({
	expertise: z.string().min(0).max(6),
	coach_type: z.string({
		required_error: 'Please select an coaching type to display.'
	}),
	bio: z.string().max(1000).min(20)
});

type CoachFormValues = z.infer<typeof coachFormSchema>;

const defaultValues: Partial<CoachFormValues> = {
	expertise: '0',
	coach_type: 'coach',
	bio: ''
};

export function CoachForm() {
	const form = useForm<CoachFormValues>({
		resolver: zodResolver(coachFormSchema),
		defaultValues,
		mode: 'onChange'
	});

	const { userId } = useAuth();
	console.log('user', userId);

	function onSubmit(data: CoachFormValues) {
		console.log('data', data);
		toast({
			title: 'You submitted the following values:',
			description: (
				<pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
					<code className="text-white">{JSON.stringify(data, null, 2)}</code>
				</pre>
			)
		});
	}

	return (
		<Card className="border-black/2">
			<CardHeader>
				<CardTitle>Coach Application</CardTitle>
			</CardHeader>
			<CardContent>
				<div className="p-4">
					<Form {...form}>
						<form
							id="coach-apply-form"
							onSubmit={form.handleSubmit(onSubmit)}
							className="space-y-8"
						>
							<FormField
								control={form.control}
								name="expertise"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Coaching Skill Preference</FormLabel>
										<Select
											onValueChange={field.onChange}
											defaultValue={`${field.value}`}
										>
											<FormControl>
												<SelectTrigger>
													<SelectValue placeholder="Select a coaching type you would prefer" />
												</SelectTrigger>
											</FormControl>
											<SelectContent>
												<SelectItem value="0">None Specified</SelectItem>
												<SelectItem value="1">Novice</SelectItem>
												<SelectItem value="2">Beginner</SelectItem>
												<SelectItem value="3">Intermediate</SelectItem>
												<SelectItem value="4">Advanced</SelectItem>
												<SelectItem value="5">Expert</SelectItem>
												<SelectItem value="6">Professional</SelectItem>
											</SelectContent>
										</Select>
										<FormDescription>
											Select your preferred coaching type. Select pacer if you plan on
											pacing athletes in any future events.
										</FormDescription>
										<FormMessage />
									</FormItem>
								)}
							/>
							<FormField
								control={form.control}
								name="coach_type"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Coaching Type</FormLabel>
										<Select onValueChange={field.onChange} defaultValue={field.value}>
											<FormControl>
												<SelectTrigger>
													<SelectValue placeholder="Select a coaching type you would prefer" />
												</SelectTrigger>
											</FormControl>
											<SelectContent>
												<SelectItem value="coach">Coach</SelectItem>
												<SelectItem value="pacer">Pacer</SelectItem>
											</SelectContent>
										</Select>
										<FormDescription>
											Select your preferred coaching type. Select pacer if you plan on
											pacing athletes in any future events.
										</FormDescription>
										<FormMessage />
									</FormItem>
								)}
							/>
							<FormField
								control={form.control}
								name="bio"
								render={({ field }) => (
									<FormItem>
										<FormLabel>Bio</FormLabel>
										<FormControl>
											<Textarea
												placeholder="Tell us a little bit about your coaching and/or pacing background"
												className="resize-none"
												{...field}
											/>
										</FormControl>
										<FormDescription>
											This will help potential clients get to know you and your
											coaching/pacing style.
										</FormDescription>
										<FormMessage />
									</FormItem>
								)}
							/>
						</form>
					</Form>
				</div>
			</CardContent>
			<CardFooter className="flex justify-end">
				<Button onClick={form.handleSubmit(onSubmit)} type="submit">
					Submit Application
				</Button>
			</CardFooter>
		</Card>
	);
}
