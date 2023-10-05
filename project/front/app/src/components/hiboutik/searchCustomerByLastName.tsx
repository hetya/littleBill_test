import React, {useEffect, useState} from 'react';
import axios from 'axios';
import '../../css/searchCustomerByLastName.css';
import  {ReactComponent as DownArrow} from '../../img/down-arrow.svg';

export default function SearchByLastName() {
    const [searchCustomerLastName, setSearchCustomerLastName] = useState('');
    const [customers, setCustomers] = useState([]);
    const [customersSalesVisibility, setCustomersSalesVisibility] = useState<{ [key: number]: boolean;}>({});
    const [error, setError] = useState('');

    const handleSearchCustomerLastNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchCustomerLastName(event.target.value);
    }

    const handleOnCustomerClick = (customers_id: number) => {
        const newCustomersSalesVisibility = {...customersSalesVisibility};
        newCustomersSalesVisibility[customers_id] = !newCustomersSalesVisibility[customers_id];
        setCustomersSalesVisibility(newCustomersSalesVisibility);
        console.log('change visibility of customer ' + customers_id + ' to ' + newCustomersSalesVisibility[customers_id]);
    }
    const handleSearchCustomer = () => {
        setError('')
        axios.get(process.env.REACT_APP_IP_BACK + '/hiboutik/search_customers_by_lastName/' + searchCustomerLastName)
            .then(response => {
                console.log(response);
                setCustomers(response.data);
                const initialVisibility: { [key: number]: boolean } = {};
                for (const customer of response.data) {
                    initialVisibility[customer.customers_id] = false;
                }
                setCustomersSalesVisibility(initialVisibility);

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
                        <div className='search-customers-customer' key={customer.customers_id} onClick={() => handleOnCustomerClick(customer.customers_id)}>
                            <div>
                                <p>{customer.last_name}</p>
                                <p>{customer.first_name}</p>
                                {customersSalesVisibility[customer.customers_id] ? <p>visibiblity true</p> : <p>visibiblity false</p>}
                            </div>
                            <DownArrow className='search-customers-customer-down-arrow'/>
                        </div>
                    ))
                }
            </div>
        </div>
    );
}