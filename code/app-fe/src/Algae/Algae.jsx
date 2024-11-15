import React, { useEffect, useState } from 'react';
import Header from '../Helpers/Header';
import VideoComponent from './VideoComponent';
import axios from 'axios';
import Loading from '../Helpers/Loading';

function Algae() {
    const [result, setResult] = useState('');
    const [loading, setLoading] = useState(true); // Corrected here
    const [isResult, setIsResult] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('token');
        axios.get('http://localhost:5000/home', {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }).then((response) => {
            setResult(response.data);
            setIsResult(true);
            setLoading(false); // Set loading to false when data is fetched
        }).catch(err => {
            setIsResult(false);
            setLoading(false); // Set loading to false even if there's an error
        });
    }, []);

    return (
        <div className="flex-1 p-10 algae-container">
            <Header title="Home" />
            {!isResult ? (
                <div className="text-center text-2xl font-bold">
                    Videos Not Found!
                </div>
            ) : (
                loading ? <Loading /> : <VideoComponent result={result} />
            )}
        </div>
    );
}

export default Algae;
