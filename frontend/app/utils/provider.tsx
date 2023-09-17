'use client';

import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';

function Providers({ children }): JSX.Element {
	const [client] = React.useState(new QueryClient());

	return <QueryClientProvider client={client}>{children}</QueryClientProvider>;
}

export default Providers;
