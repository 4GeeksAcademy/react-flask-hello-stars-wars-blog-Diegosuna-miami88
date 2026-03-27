import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";




export const Home = () => {

	const { store, dispatch } = useGlobalReducer()

	const login = async (username, password) => {
		const resp = await fetch(`https://your_api.com/token`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ username, password })
		})

		if (!resp.ok) throw Error("There was a problem in the login request")

		if (resp.status === 401) {
			throw ("Invalid credentials")
		}
		else if (resp.status === 400) {
			throw ("Invalid email or password format")
		}
		const data = await resp.json()
		// Save your token in the localStorage
		// Also you should set your user into the store using the setItem function
		localStorage.setItem("jwt-token", data.token);

		return data
	}

	const loadMessage = async () => {
		try {
			const backendUrl = import.meta.env.VITE_BACKEND_URL

			if (!backendUrl) throw new Error("VITE_BACKEND_URL is not defined in .env file")

			const response = await fetch(backendUrl + "/api/hello")
			const data = await response.json()

			if (response.ok) dispatch({ type: "set_hello", payload: data.message })

			return data

		} catch (error) {
			if (error.message) throw new Error(
				`Could not fetch the message from the backend.
				Please check if the backend is running and the backend port is public.`
			);
		}

	}

	useEffect(() => {
		loadMessage()
	}, [])

	return (
		<div className="text-center mt-5">
			<h1 className="display-4">Hello Rigo!!</h1>
			<p className="lead">
				<img src={rigoImageUrl} className="img-fluid rounded-circle mb-3" alt="Rigo Baby" />
			</p>
			<div className="alert alert-info">
				{store.message ? (
					<span>{store.message}</span>
				) : (
					<span className="text-danger">
						Loading message from the backend (make sure your python 🐍 backend is running)...
					</span>
				)}
			</div>
		</div>
	);
}; 