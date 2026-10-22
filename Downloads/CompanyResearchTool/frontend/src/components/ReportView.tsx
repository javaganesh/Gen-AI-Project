function ReportView({
  report,
}: any) {
  return (
    <div>

      <h2>
        Company Overview
      </h2>

      <p>
        {report.overview}
      </p>

      <h2>
        Key People
      </h2>

      <ul>
        {report.key_people?.map(
          (
            person: any,
            index: number
          ) => (
            <li key={index}>
              {person.name} -
              {" "}
              {person.title}
            </li>
          )
        )}
      </ul>

      <h2>
        Recent News
      </h2>

      <ul>
        {report.news?.map(
          (
            news: string,
            index: number
          ) => (
            <li key={index}>
              {news}
            </li>
          )
        )}
      </ul>

      <h2>
        Financial Highlights
      </h2>

      <pre>
        {JSON.stringify(
          report.financials,
          null,
          2
        )}
      </pre>

      <h2>
        Risk Factors
      </h2>

      <ul>
        {report.risks?.map(
          (
            risk: string,
            index: number
          ) => (
            <li key={index}>
              {risk}
            </li>
          )
        )}
      </ul>

    </div>
  );
}

export default ReportView;