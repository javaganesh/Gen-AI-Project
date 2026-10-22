interface Props {
  reports: any[];
  loadReport: (id: number) => void;
  deleteReport: (id: number) => void;
}

function ReportHistory({
  reports,
  loadReport,
  deleteReport
}: Props) {

  return (
    <div>

      <h2>Report History</h2>

      {
        reports.map(
          (report) => (
            <div key={report.id}>

              <button
                onClick={() =>
                  loadReport(report.id)
                }
              >
                {report.company_name}
              </button>

              <button
                onClick={() =>
                  deleteReport(report.id)
                }
              >
                Delete
              </button>

            </div>
          )
        )
      }

    </div>
  );
}

export default ReportHistory;