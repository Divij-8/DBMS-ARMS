import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE || "http://localhost:8000/api",
  withCredentials: false,
  headers: { "Content-Type": "application/json" }
});

export default api;
