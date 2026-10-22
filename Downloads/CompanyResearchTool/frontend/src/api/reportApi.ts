import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const getReports = async () => {
  const response = await axios.get(`${API_URL}/reports`);
  return response.data;
};

export const getReport = async (id: number) => {
  const response = await axios.get(`${API_URL}/reports/${id}`);
  return response.data;
};

export const deleteReport = async (id: number) => {
  await axios.delete(`${API_URL}/reports/${id}`);
};