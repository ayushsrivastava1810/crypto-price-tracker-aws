import axios from "axios";

const API = axios.create({
  baseURL: "http://44.222.191.142:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Attach token if exists
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});

export default API;
