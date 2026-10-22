export interface KeyPerson {
  name: string;
  title: string;
}

export interface Financials {
  revenue: string | null;
  employee_count: string | null;
  market_cap: string | null;
  yoy_growth: string | null;
}

export interface Report {
  overview: string;
  key_people: KeyPerson[];
  news: string[];
  financials: Financials;
  risks: string[];
}