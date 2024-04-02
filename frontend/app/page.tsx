"use client";

import InputSection from "@/components/InputSection";
import { useState } from "react";

export default function Home() {
  const [companies, setCompanies] = useState<string[]>([]);
  const [positions, setPositions] = useState<string[]>([]);
  return (
    <div className="bg-white min-h-screen text-black">
      <div className="flex">
        <div className="w-1/2 p-4">
          <InputSection
            title="Companies"
            placeholder="Add a company"
            data={companies}
            setData={setCompanies}
          />

          <InputSection
            title="Positions"
            placeholder="Add a position"
            data={positions}
            setData={setPositions}
          />
        </div>
        <div></div>
      </div>
    </div>
  );
}
