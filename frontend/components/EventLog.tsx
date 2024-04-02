import { EventType } from "@/hooks/useCrewJob";
import React from "react";

type EventLogProps = {
  events: EventType[];
};

function EventLog({ events }: EventLogProps) {
  return (
    <div className="flex flex-col h-full">
        <h2>Event Details</h2>
    </div>
  )
}

export default EventLog;
