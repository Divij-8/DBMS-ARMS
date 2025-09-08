import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import FarmerRegistration from "./pages/FarmerRegistration";
import CropTracker from "./pages/CropTracker";
import FertilizerLogs from "./pages/FertilizerLogs";
import EquipmentRental from "./pages/EquipmentRental";
import SchemeApplications from "./pages/SchemeApplications";
import Reports from "./pages/Reports";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import "./styles/App.css";

export default function App() {
  return (
    <div className="app">
      <Navbar />
      <nav className="container">
        <Link to="/">Farmers</Link> |{" "}
        <Link to="/crops">Crops</Link> |{" "}
        <Link to="/fertilizers">Fertilizers</Link> |{" "}
        <Link to="/equipment">Equipment</Link> |{" "}
        <Link to="/schemes">Schemes</Link> |{" "}
        <Link to="/reports">Reports</Link>
      </nav>
      <main className="container">
        <Routes>
          <Route path="/" element={<FarmerRegistration />} />
          <Route path="/crops" element={<CropTracker />} />
          <Route path="/fertilizers" element={<FertilizerLogs />} />
          <Route path="/equipment" element={<EquipmentRental />} />
          <Route path="/schemes" element={<SchemeApplications />} />
          <Route path="/reports" element={<Reports />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}
