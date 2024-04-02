import axios from "axios";
import React, { useEffect, useState } from "react";
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
  const [positionInfo, setPositionInfo] = useState<PositionInfo[]>([]);
  const [running, setRunning] = useState<boolean>(false);
  const [currentJobId, setCurrentJobId] = useState<string>("");

  useEffect(() => {
    let intervalId: number;
    const fetchJobStatus = async () => {
      try {
        const response = await axios.get<{
          result: { positions: PositionInfo[] };
          events: EventType[];
          status: string;
        }>(`http://localhost:3001/api/crew/${currentJobId}`);

        console.log(response.data);

        const { result, events: fetchedEvents, status } = response.data;

        setEvents(fetchedEvents);

        if (result) {
          console.log(result);
          setPositionInfo(result.positions);
        }

        if (status === "COMPLETE" || status === "ERROR") {
          if (intervalId) clearInterval(intervalId);
          setRunning(false);
          toast.success(`Job with id ${currentJobId} completed`);
        }
      } catch (error) {
        console.error(error);
        setCurrentJobId("");
        setRunning(false);
        toast.error(`Job with id ${currentJobId} failed to complete`);
      }
    };

    if (currentJobId !== "") {
      intervalId = setInterval(fetchJobStatus, 1000) as unknown as number;
    }
  }, [currentJobId]);

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
    startJob,
    events,
    positionInfo,
    running,
  };
}

export default useCrewJob;
