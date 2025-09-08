import React, { useEffect, useState } from "react";
import { listFarmers, createFarmer } from "../api/farmerApi";

export default function FarmerRegistration() {
  const [farmers, setFarmers] = useState([]);
  const [form, setForm] = useState({ name: "", phone: "", address: "" });

  const refresh = async () => {
    const { data } = await listFarmers();
    setFarmers(data);
  };

  useEffect(() => { refresh(); }, []);

  const submit = async (e) => {
    e.preventDefault();
    await createFarmer(form);
    setForm({ name: "", phone: "", address: "" });
    refresh();
  };

  return (
    <div>
      <h2>Farmer Registration</h2>
      <form onSubmit={submit}>
        <input placeholder="Name" value={form.name} onChange={e => setForm({...form, name: e.target.value})} required />
        <input placeholder="Phone" value={form.phone} onChange={e => setForm({...form, phone: e.target.value})} />
        <input placeholder="Address" value={form.address} onChange={e => setForm({...form, address: e.target.value})} />
        <button type="submit">Add</button>
      </form>
      <ul>
        {farmers.map(f => (<li key={f.id}>{f.name} - {f.phone}</li>))}
      </ul>
    </div>
  );
}
