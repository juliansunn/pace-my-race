import Navbar from '../../components/Navbar';
import Sidebar from '../../components/Sidebar';

const DashboardLayout = async ({ children }: { children: React.ReactNode }) => {
	return (
		<div className="h-full relative ">
			<div className="hidden h-full md:flex md:w-72 md:flex-col md:fixed md:inset-y-0 z-8">
				<Sidebar />
			</div>
			<main className="md:pl-72 pb-10">
				<Navbar />
				<div className="flex flex-col h-full w-full rounded-lg px-4 space-y-4">
					{children}
				</div>
			</main>
		</div>
	);
};

export default DashboardLayout;
