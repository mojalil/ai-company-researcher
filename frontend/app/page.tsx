"use client";

import EventLog from "@/components/EventLog";
import { FinalOutput } from "@/components/FinalOutput";
import InputSection from "@/components/InputSection";
import { useCrewJob } from "@/hooks/useCrewJob";


export default function Home() {
  const crewJob = useCrewJob();
  const { positions, setPositions, companies, setCompanies, events } = crewJob;
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
        <div className="w-1/2 p-4 flex flex-col">
          <div className=" justify-between flex items-center mb-4">
            <h2 className="text-2xl font-bold">Output</h2>
            <button 
            disabled={crewJob.running}
            
            className="bg-blue-500 hover:bg-blue-700 text-white py-2 rounded-lg px-4"
            onClick={crewJob.startJob}
            >
              {crewJob.running ? "Running..." : "Start"}
            </button>
          </div>
          {/* FINAL OUTPUT */}
          <FinalOutput positionInfoList={crewJob.positionInfoList} />
          {/* EVENT LOG */}
          <EventLog events={events} />
        </div>
      </div>
    </div>
  );
}
