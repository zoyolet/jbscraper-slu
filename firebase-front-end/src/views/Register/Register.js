import React, {useState} from 'react';
import { Form } from '@unform/web';
import { Link } from 'react-router-dom';
import { Input } from '../../components';
import { parseErrorMessage } from '../validations/parseFirebaseLoginErrors';
import { createUserWithEmailAndPassword } from '../functions/firebaseFunctions';

import './Register.css';

export default function Register({ history }) {
    const [error, setError] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    async function handleSubmit(data) {
        setIsLoading(!isLoading);

        const { email, password } = data;
        try {
            await createUserWithEmailAndPassword(email, password);
            history.push('/');
        } catch (error) {
            const parsedError = await parseErrorMessage(error);
            setError(parsedError);
            setIsLoading(!isLoading);
            setIsLoading(isLoading);
        }
    }

    return (
        <div className="container">
            <h1>Register</h1>
            <div className="form-container">
                <Form onSubmit={handleSubmit}>
                    <Input name="email" type="email" placeholder="Email To Register"/>
                    <Input name="password" type="password" placeholder="Set Password"/>
                    {!isLoading && (
                        <button type="submit">Submit</button>
                    )}
                    {isLoading && (
                        <button type="button" disabled>Please wait...</button>
                    )}
                </Form>
                {error && (
                    <span>{error}</span>
                )}
                <div className="link-container">
                    <Link to='/'>Login Page</Link>
                    <Link to='/reset-password'>Reset Password</Link>
                </div>
            </div>
        </div>
    )
}
