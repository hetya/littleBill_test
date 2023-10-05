import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../../css/searchCustomerByLastName.css';

export default function SearchByLastName() {
    const [searchCustomerLastName, setSearchCustomerLastName] = useState('');
    const [customers, setCustomers] = useState([]);
    const [error, setError] = useState('');

    const handleSearchCustomerLastNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchCustomerLastName(event.target.value);
    }

    const handleSearchCustomer = () => {
        setError('')
        axios.get(process.env.REACT_APP_IP_BACK + '/hiboutik/search_customers_by_lastName/' + searchCustomerLastName)
            .then(response => {
                console.log(response);
                setCustomers(response.data);
            })
            .catch(error => {
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
        setSearchCustomerLastName('')
    }

    return (
        <div className='search-customers-component'>
            <div className='search-customers-header'>
                <h3>Search :</h3>
                <input className='search-customers-input-and-button' type="text" placeholder="Customer Lastname" value={searchCustomerLastName} onChange={handleSearchCustomerLastNameChange}/>
                <button className='search-customers-input-and-button search-customers-button' onClick={handleSearchCustomer}>Search</button>
            </div>
            {error ? <p className=''>*{error}</p> : null}
            <div className='search-customers-list'>
                {
                    customers.map((customer : any) => (
                        <div className='search-customers-customer' key={customer.customers_id}>
                            <p>{customer.last_name}</p>
                            <p>{customer.first_name}</p>
                        </div>
                    ))
                }
            </div>
        </div>
    );
}