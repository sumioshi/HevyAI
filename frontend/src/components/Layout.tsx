import React, { ReactNode } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
  HomeIcon, 
  ClipboardDocumentListIcon, 
  QueueListIcon,
  Squares2X2Icon
} from '@heroicons/react/24/outline';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const location = useLocation();
  
  const isActive = (path: string) => {
    return location.pathname === path 
      ? 'bg-hevy-blue text-white' 
      : 'text-gray-600 hover:bg-gray-100';
  };

  return (
    <div className="min-h-screen flex">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md">
        <div className="p-4">
          <h1 className="text-2xl font-bold text-hevy-blue">HevyAI</h1>
        </div>
        <nav className="mt-6">
          <Link to="/" className={`flex items-center px-4 py-3 ${isActive('/')}`}>
            <HomeIcon className="h-5 w-5 mr-3" />
            <span>Dashboard</span>
          </Link>
          <Link to="/workouts" className={`flex items-center px-4 py-3 ${isActive('/workouts')}`}>
            <ClipboardDocumentListIcon className="h-5 w-5 mr-3" />
            <span>Treinos</span>
          </Link>
          <Link to="/routines" className={`flex items-center px-4 py-3 ${isActive('/routines')}`}>
            <QueueListIcon className="h-5 w-5 mr-3" />
            <span>Rotinas</span>
          </Link>
          <Link to="/exercise-templates" className={`flex items-center px-4 py-3 ${isActive('/exercise-templates')}`}>
            <Squares2X2Icon className="h-5 w-5 mr-3" />
            <span>Exercícios</span>
          </Link>
        </nav>
      </div>
      
      {/* Main Content */}
      <div className="flex-1 bg-gray-50">
        <header className="bg-white shadow-sm">
          <div className="px-6 py-4">
            <h2 className="text-xl font-semibold text-gray-800">
              {location.pathname === '/' && 'Dashboard'}
              {location.pathname === '/workouts' && 'Treinos'}
              {location.pathname.startsWith('/workouts/') && 'Detalhes do Treino'}
              {location.pathname === '/routines' && 'Rotinas'}
              {location.pathname.startsWith('/routines/') && 'Detalhes da Rotina'}
              {location.pathname === '/exercise-templates' && 'Modelos de Exercícios'}
            </h2>
          </div>
        </header>
        <main className="p-6">
          {children}
        </main>
      </div>
    </div>
  );
};

export default Layout;