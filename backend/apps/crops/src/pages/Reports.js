import React, { useEffect, useState } from "react";
import { summary } from "../api/reportApi";
import DashboardCard from "../components/DashboardCard";

export default function Reports() {
  const [data, setData] = useState(null);
  useEffect(() => {
    (async () => {
      const { data } = await summary();
      setData(data);
    })();
  }, []);
  if (!data) return <div>Loading...</div>;
  return (
    <div>
      <h2>Reports</h2>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 16 }}>
        {Object.entries(data).map(([k, v]) => (
          <DashboardCard key={k} title={k} value={v} />
        ))}
      </div>
    </div>
  );
}
