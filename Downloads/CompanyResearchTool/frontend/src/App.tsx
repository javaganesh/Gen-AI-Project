import { useEffect, useState } from "react";

import SearchBar from "./components/SearchBar";
import ReportView from "./components/ReportView";
import ReportHistory from "./components/ReportHistory";
import Loader from "./components/Loader";

import {
  getReports,
  getReport,
  deleteReport,
} from "./api/reportApi";

function App() {
  const [company, setCompany] = useState("");

  const [loading, setLoading] = useState(false);

  const [reports, setReports] = useState<any[]>([]);

  const [report, setReport] = useState<any>({
    overview: "",
    key_people: [],
    news: [],
    financials: {},
    risks: [],
  });

  const fetchReports = async () => {
    try {
      const data = await getReports();
      setReports(data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchReports();
  }, []);

  const startResearch = async () => {
    if (!company.trim()) {
      alert("Please enter company name");
      return;
    }

    setLoading(true);

    setReport({
      overview: "",
      key_people: [],
      news: [],
      financials: {},
      risks: [],
    });

    const response = await fetch(
      `http://localhost:8000/api/research?company_name=${company}`
    );

    const reader = response.body?.getReader();

    if (!reader) {
      setLoading(false);
      return;
    }

    const decoder = new TextDecoder();

    while (true) {
      const { done, value } =
        await reader.read();

      if (done) break;

      const chunk = decoder.decode(value);

      const lines =
        chunk.split("\n");

      let eventName = "";
      let eventData = "";

      for (const line of lines) {
        if (
          line.startsWith("event:")
        ) {
          eventName = line
            .replace("event:", "")
            .trim();
        }

        if (
          line.startsWith("data:")
        ) {
          eventData = line
            .replace("data:", "")
            .trim();
        }

        if (
          eventName &&
          eventData
        ) {
          updateReport(
            eventName,
            eventData
          );

          eventName = "";
          eventData = "";
        }
      }
    }

    setLoading(false);

    fetchReports();
  };

  const updateReport = (
    eventName: string,
    eventData: string
  ) => {
    setReport(
      (prev: any) => {
        const updated = {
          ...prev,
        };

        switch (
          eventName
        ) {
          case "overview":
            updated.overview =
              eventData;
            break;

          case "key_people":
            updated.key_people =
              JSON.parse(
                eventData
              );
            break;

          case "news":
            updated.news =
              JSON.parse(
                eventData
              );
            break;

          case "financials":
            updated.financials =
              JSON.parse(
                eventData
              );
            break;

          case "risks":
            updated.risks =
              JSON.parse(
                eventData
              );
            break;

          default:
            break;
        }

        return updated;
      }
    );
  };

  const loadReportData =
    async (
      id: number
    ) => {
      const data =
        await getReport(id);

      setReport({
        ...data,

        key_people:
          JSON.parse(
            data.key_people
          ),

        news:
          JSON.parse(
            data.news
          ),

        financials:
          JSON.parse(
            data.financials
          ),

        risks:
          JSON.parse(
            data.risks
          ),
      });
    };

  const removeReport =
    async (
      id: number
    ) => {
      await deleteReport(id);

      fetchReports();
    };

  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "0 auto",
        padding: "20px",
      }}
    >
      <h1>
        Company Research Tool
      </h1>

      <SearchBar
        company={company}
        setCompany={
          setCompany
        }
        startResearch={
          startResearch
        }
      />

      {loading && (
        <Loader />
      )}

      <ReportView
        report={report}
      />

      <ReportHistory
        reports={reports}
        loadReport={
          loadReportData
        }
        deleteReport={
          removeReport
        }
      />
    </div>
  );
}

export default App;