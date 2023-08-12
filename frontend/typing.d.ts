interface Race {
	id: number;
	name: string;
	link: string;
	image: string;
	description: string;
	registration_open: boolean;
	registration_deadline: Date;
	race_start: Date;
	type: string | null;
	city: string | null;
	participants: number[];
}

interface RacesResponse {
	page: number;
	page_size: number;
	total_count: number;
	results: Race[];
}
