import api from "./axiosConfig";
export const summary = () => api.get("/reports/summary/");
