import React, { useState } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer";


export const LogIn = () => {
    const BASE_URL = import.meta.env.VITE_BACKEND_URL
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [logInFailed, setLogInFailed] = useState(false)

    const handleLogin = async () => {
        const Response = await fetch(BASE_URL + "/login", {
            method: "POST",
            headers: {
                "content-Type": "application/json"
            },
            body: JSON.stringinify(
                {
                    "email": email,
                    "pasword": password
                }
            )
        })
        if (!Response.ok) {
            setLogInFailed(true)
            return
        }
        const data = await Response.json()
        localStorage.settings("token", data.token)
        setLogInFailed(false)

    }

    return (
        <>
            <div className="container">
                <h1>LogIn page!</h1>
                {logInFailed ? <h2 className="text-danger">logIn Failed</h2> : null}
                <div className="row">
                    <div className="col-3"></div>
                    <div className="col-6">
                        <div>
                            <label for="email">Email</label>
                            <input type="text" name="email" onChange={e => setEmail(e.target.value)} value={email} />
                        </div>
                        <div>
                            <label for="password">password</label>
                            <input type="password" name="password" onChange={e => setPassword(e.target.value)} value={password} />
                        </div>
                    </div>
                    <div className="col-3"></div>
                </div>
                <button className="btn btn-success" onClick={handleSignUp}>Sign up</button>
            </div>
        </>
    )
}