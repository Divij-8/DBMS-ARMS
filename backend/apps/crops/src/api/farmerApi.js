import api from "./axiosConfig";
export const listFarmers = () => api.get("/farmers/");
export const createFarmer = (data) => api.post("/farmers/", data);
