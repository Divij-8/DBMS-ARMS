import api from "./axiosConfig";
export const listEquipment = () => api.get("/equipment/");
export const listRentals = () => api.get("/rentals/");
