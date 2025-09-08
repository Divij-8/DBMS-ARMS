import api from "./axiosConfig";
export const listFertilizerLogs = () => api.get("/fertilizer-logs/");
