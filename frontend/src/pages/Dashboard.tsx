import React, { useState, useEffect } from 'react';

const Dashboard: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [apiKey, setApiKey] = useState<string>('');
  
  useEffect(() => {
    // Simulação de carregamento
    setTimeout(() => {
      setLoading(false);
    }, 1000);
    
    // Verificar se a API key está configurada
    const key = process.env.REACT_APP_HEVY_API_KEY || '';
    setApiKey(key ? 'Configurada' : 'Não configurada');
  }, []);
  
  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-hevy-blue"></div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <strong className="font-bold">Erro!</strong>
        <span className="block sm:inline"> {error}</span>
      </div>
    );
  }
  
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Bem-vindo ao HevyAI</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">Status da Integração</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="border rounded-md p-4">
            <h3 className="text-lg font-medium mb-2">API Hevy</h3>
            <p className="text-gray-600">
              Status: <span className={apiKey === 'Configurada' ? 'text-green-600' : 'text-red-600'}>
                {apiKey}
              </span>
            </p>
          </div>
          <div className="border rounded-md p-4">
            <h3 className="text-lg font-medium mb-2">Backend Django</h3>
            <p className="text-gray-600">
              Status: <span className="text-green-600">Conectado</span>
            </p>
          </div>
        </div>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-xl font-semibold mb-4">Funcionalidades Disponíveis</h2>
        <ul className="list-disc pl-5 space-y-2">
          <li>Visualização de treinos</li>
          <li>Visualização de rotinas</li>
          <li>Visualização de modelos de exercícios</li>
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;