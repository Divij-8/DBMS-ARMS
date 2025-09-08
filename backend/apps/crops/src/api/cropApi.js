import api from "./axiosConfig";
export const listCrops = () => api.get("/crops/");
export const createCrop = (data) => api.post("/crops/", data);
