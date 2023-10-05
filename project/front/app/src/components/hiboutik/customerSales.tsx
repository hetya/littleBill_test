import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../../css/customerSales.css';
import  {ReactComponent as RightArrow} from '../../img/right-arrow.svg';
import  {ReactComponent as LeftArrow} from '../../img/left-arrow.svg';

export default function CustomerSales({customers_id} : {customers_id: string}) {
    const [customerSales, setCustomerSales] = useState([]);
    const [pageNumber, setPageNumber] = useState(1);
    const [error, setError] = useState('');

    const handleNextPage = () => {
        if (customerSales.length > 0)
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
    },[pageNumber]);

    return (
        <div className=''>
            <div className='customer-sales-header'>
                <p>Sales :</p>
                {error ? <p className='app-error'>*{error}</p> : null}
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
                <div className='customer-sales-arrows'>
                    <LeftArrow className='customer-sales-arrow' onClick={handlePreviousPage}/>
                    <RightArrow className='customer-sales-arrow' onClick={handleNextPage}/>
                </div>
            </div>
        </div>
    );
}