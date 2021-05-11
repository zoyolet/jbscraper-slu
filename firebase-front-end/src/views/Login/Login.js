import React, { useState } from 'react';
import { Form } from '@unform/web';
import { Link } from 'react-router-dom';
import { Input } from '../../components';
import { parseErrorMessage } from '../validations/parseFirebaseLoginErrors';
import { signInWithEmailAndPassword } from '../functions/firebaseFunctions';

import './Login.css';

export default function Login({ history }) {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(false);

    async function handleSubmit(data) {
        setIsLoading(!isLoading);

        const { email, password } = data;
        try {
            await signInWithEmailAndPassword(email, password);
            history.push('/home');
        } catch (error) {
            const parsedError = await parseErrorMessage(error);
            setError(parsedError);
            setIsLoading(isLoading);
        }
    }

    return (
        <div className="container">
            <h1>Login Page</h1>
            <div className="form-container">
                <Form onSubmit={handleSubmit}>
                    <Input name="email" type="email" placeholder="Email" />
                    <Input name="password" type="password" placeholder="Password" />
                    {!isLoading && (
                        <button type="submit">Enter</button>
                    )}
                    {isLoading && (
                        <button type="button" disabled>Please wait...</button>
                    )}
                </Form>
                {error && (
                    <span>{error}</span>
                )}
                <div className="link-container">
                    <Link to='/register'>Register New</Link>
                    <Link to='/reset-password'>Reset Password</Link>
                </div>
            </div>
        </div>
    )
}
