import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { ClockIcon, CalendarIcon } from '@heroicons/react/24/outline';

interface Set {
  id: string;
  reps?: number;
  weight?: number;
  duration?: number;
  distance?: number;
  rpe?: number;
  completed: boolean;
}

interface Exercise {
  id: string;
  exercise_template_id: string;
  name: string;
  notes?: string;
  sets: Set[];
}

interface Workout {
  id: string;
  name: string;
  exercises: Exercise[];
  notes?: string;
  start_time?: string;
  end_time?: string;
  created_at?: string;
  updated_at?: string;
}

const WorkoutList: React.FC = () => {
  const [workouts, setWorkouts] = useState<Workout[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [page, setPage] = useState<number>(1);
  const [totalPages, setTotalPages] = useState<number>(1);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        setLoading(true);
        // Em um ambiente real, você faria chamadas reais à API
        // const response = await axios.get(`/api/workouts?page=${page}&per_page=10`);
        
        // Para este exemplo, vamos simular os dados
        // Simular um pequeno atraso para mostrar o estado de loading
        await new Promise(resolve => setTimeout(resolve, 500));
        
        const mockWorkouts: Workout[] = [
          {
            id: '1',
            name: 'Treino de Peito e Tríceps',
            exercises: [
              {
                id: '1',
                exercise_template_id: '101',
                name: 'Supino Reto',
                sets: [
                  { id: '1', reps: 12, weight: 60, completed: true },
                  { id: '2', reps: 10, weight: 70, completed: true },
                  { id: '3', reps: 8, weight: 80, completed: true }
                ]
              },
              {
                id: '2',
                exercise_template_id: '102',
                name: 'Tríceps Corda',
                sets: [
                  { id: '4', reps: 15, weight: 30, completed: true },
                  { id: '5', reps: 12, weight: 35, completed: true }
                ]
              }
            ],
            start_time: '2025-05-10T18:00:00.000Z',
            end_time: '2025-05-10T19:15:00.000Z',
            created_at: '2025-05-10T18:00:00.000Z'
          },
          {
            id: '2',
            name: 'Treino de Costas e Bíceps',
            exercises: [
              {
                id: '3',
                exercise_template_id: '103',
                name: 'Puxada Frontal',
                sets: [
                  { id: '6', reps: 12, weight: 50, completed: true },
                  { id: '7', reps: 10, weight: 60, completed: true },
                  { id: '8', reps: 8, weight: 70, completed: true }
                ]
              },
              {
                id: '4',
                exercise_template_id: '104',
                name: 'Rosca Direta',
                sets: [
                  { id: '9', reps: 15, weight: 25, completed: true },
                  { id: '10', reps: 12, weight: 30, completed: true }
                ]
              }
            ],
            start_time: '2025-05-08T19:00:00.000Z',
            end_time: '2025-05-08T20:30:00.000Z',
            created_at: '2025-05-08T19:00:00.000Z'
          }
        ];
        
        setWorkouts(mockWorkouts);
        setTotalPages(3); // Simulando que temos 3 páginas no total
      } catch (error) {
        console.error('Erro ao buscar treinos:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchWorkouts();
  }, [page]);
  
  const formatDate = (dateString?: string) => {
    if (!dateString) return 'Data não disponível';
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR', { 
      day: '2-digit', 
      month: '2-digit',
      year: 'numeric' 
    });
  };
  
  const formatDuration = (startTime?: string, endTime?: string) => {
    if (!startTime || !endTime) return 'Duração não disponível';
    
    const start = new Date(startTime);
    const end = new Date(endTime);
    const durationMs = end.getTime() - start.getTime();
    const durationMin = Math.floor(durationMs / 60000);
    
    const hours = Math.floor(durationMin / 60);
    const minutes = durationMin % 60;
    
    return hours > 0 
      ? `${hours}h ${minutes}min` 
      : `${minutes}min`;
  };
  
  const calculateTotalSets = (exercises: Exercise[]) => {
    return exercises.reduce((total, exercise) => total + exercise.sets.length, 0);
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-hevy-blue"></div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Meus Treinos</h1>
      </div>
      
      {workouts.length === 0 ? (
        <div className="bg-white p-6 rounded-lg shadow-md text-center">
          <p className="text-gray-600">Nenhum treino encontrado.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-6">
          {workouts.map(workout => (
            <Link 
              key={workout.id} 
              to={`/workouts/${workout.id}`}
              className="block bg-white rounded-lg shadow-md hover:shadow-lg transition"
            >
              <div className="p-6">
                <div className="flex justify-between items-start">
                  <h2 className="text-xl font-semibold text-gray-800">{workout.name}</h2>
                  <div className="bg-gray-100 px-3 py-1 rounded-full text-sm text-gray-600">
                    {workout.exercises.length} exercícios
                  </div>
                </div>
                
                <div className="mt-4 space-y-2">
                  {workout.exercises.slice(0, 3).map(exercise => (
                    <div key={exercise.id} className="flex justify-between items-center">
                      <span className="text-gray-700">{exercise.name}</span>
                      <span className="text-gray-500 text-sm">{exercise.sets.length} séries</span>
                    </div>
                  ))}
                  
                  {workout.exercises.length > 3 && (
                    <div className="text-gray-500 text-sm">
                      + {workout.exercises.length - 3} exercícios
                    </div>
                  )}
                </div>
                
                <div className="flex items-center mt-5 pt-5 border-t border-gray-100 text-sm text-gray-600">
                  <div className="flex items-center mr-6">
                    <CalendarIcon className="h-4 w-4 mr-1" />
                    <span>{formatDate(workout.start_time)}</span>
                  </div>
                  <div className="flex items-center">
                    <ClockIcon className="h-4 w-4 mr-1" />
                    <span>{formatDuration(workout.start_time, workout.end_time)}</span>
                  </div>
                  <div className="ml-auto">
                    <span>Total: {calculateTotalSets(workout.exercises)} séries</span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
      
      {/* Paginação */}
      <div className="flex justify-center mt-8">
        <nav className="inline-flex rounded-md shadow">
          <button
            onClick={() => setPage(prev => Math.max(prev - 1, 1))}
            disabled={page === 1}
            className={`px-4 py-2 rounded-l-md ${
              page === 1 
                ? 'bg-gray-100 text-gray-400 cursor-not-allowed' 
                : 'bg-white text-gray-700 hover:bg-gray-50'
            }`}
          >
            Anterior
          </button>
          
          {Array.from({ length: totalPages }, (_, i) => i + 1).map(p => (
            <button
              key={p}
              onClick={() => setPage(p)}
              className={`px-4 py-2 ${
                p === page
                  ? 'bg-hevy-blue text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-50'
              }`}
            >
              {p}
            </button>
          ))}
          
          <button
            onClick={() => setPage(prev => Math.min(prev + 1, totalPages))}
            disabled={page === totalPages}
            className={`px-4 py-2 rounded-r-md ${
              page === totalPages 
                ? 'bg-gray-100 text-gray-400 cursor-not-allowed' 
                : 'bg-white text-gray-700 hover:bg-gray-50'
            }`}
          >
            Próxima
          </button>
        </nav>
      </div>
    </div>
  );
};

export default WorkoutList;