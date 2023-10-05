import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../../css/customerSales.css';

export default function CustomerSales({customers_id} : {customers_id: string}) {
    const [customerSales, setCustomerSales] = useState([]);
    const [pageNumber, setPageNumber] = useState(1);
    const [error, setError] = useState('');

    const handleNextPage = () => {
        setPageNumber(pageNumber + 1);
    }

    const handlePreviousPage = () => {
        if (pageNumber > 1)
            setPageNumber(pageNumber - 1);
    }
    useEffect(() => {
        setError('')
        axios.get(process.env.REACT_APP_IP_BACK + '/hiboutik/get_customer_sales/' + customers_id + '/' + pageNumber)
            .then(response => {
                console.log(response);
                setCustomerSales(response.data);
            })
            .catch(error => {
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
    },[]);

    return (
        <div className=''>
            <div className='customer-sales-header'>
                <p>Sales :</p>
                {error ? <p className=''>*{error}</p> : null}
            </div>
            <div className=''>
                {
                    customerSales.map((customerSale : any) => (
                        <div>
                            <div className='customer-sales-list-separator'></div>
                            <div className='customer-sales-list-sale' key={customerSale.sale_id}>
                                <p>{customerSale.completed_at}</p>
                                <div className='customer-sales-list-sale-price'>
                                    <p>{customerSale.total}</p>
                                    <p>{customerSale.currency}</p>
                                </div>
                            </div>
                        </div>
                    ))
                }
            </div>
        </div>
    );
}