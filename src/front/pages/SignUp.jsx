import React, { useState } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer";

export const SignUp = () => {
    const BASE_URL = import.meta.env.VITE_BACKEND_URL
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [signUpFailed, setSignUpFailed] = useState(false)


    const handleSignUp = async () => {
        const Response = await fetch(BASE_URL + "/signup", {
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
            setSignUpFailed(true)
            return
        }
        const data = await Response.json()
        return data
    }


    return (
        <>
            <div className="container">
                <h1>Hello from the Signup page</h1>
                {signUpFailed ? <h2 className="text-danger">Sign up failed</h2> : null}
                <div className="row">
                    <div className="col-3"></div>
                    <div className="col-6">
                        <div>
                            <label for="email">Email</label>
                            <input type="text" name="email" onChange = {e => setEmail(e.target.value)} value={email} />
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