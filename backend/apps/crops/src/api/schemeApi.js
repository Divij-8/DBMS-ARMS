import api from "./axiosConfig";
export const listSchemes = () => api.get("/schemes/");
export const listApplications = () => api.get("/scheme-applications/");
