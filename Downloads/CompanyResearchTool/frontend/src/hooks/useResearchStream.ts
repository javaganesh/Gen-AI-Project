export const startResearchStream = (
  companyName: string,
  onUpdate: (data: any) => void
) => {

  const eventSource =
    new EventSource(
      `http://localhost:8000/api/research?company_name=${companyName}`
    );

  eventSource.onmessage =
    (event) => {
      onUpdate(event.data);
    };

  return eventSource;
};