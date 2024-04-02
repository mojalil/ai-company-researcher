import axios from "axios";
import React, { useState } from "react";
import toast from "react-hot-toast";

type EventType = {
  data: string;
  timestamp: string;
};

export type NamedUrls = {
  name: string;
  url: string[];
};

export type PositionInfo = {
  company: string;
  position: string;
  name: string;
  blog_articles: string[];
  youtube_interviews: NamedUrls[];
};

export type PositionInfoList = {
  positions: PositionInfo[];
};

function useCrewJob() {
  const [companies, setCompanies] = useState<string[]>([]);
  const [positions, setPositions] = useState<string[]>([]);
  const [events, setEvents] = useState<EventType[]>([]);
  const [positionInfo, setPositionInfo] = useState<PositionInfoList[]>([]);
  const [running, setRunning] = useState<boolean>(false);
  const [currentJobId, setCurrentJobId] = useState<string>("");

  const startJob = async () => {
    // clean up the old job
    setEvents([]);
    setPositionInfo([]);
    setRunning(true);

    // request to our backend
    try {
      const response = await axios.post<{ job_id: string }>(
        "http://localhost:3001/api/crew",
        {
          companies,
          positions,
        }
      );

      toast.success("Job started");

      setCurrentJobId(response.data.job_id);
    } catch (error) {
      console.error(error);
      setCurrentJobId("");
      setRunning(false);

      toast.error("Job failed to start");
    }
  };
  // update out state

  return {
    companies,
    setCompanies,
    positions,
    setPositions,
    startJob
  };
}

export default useCrewJob;
