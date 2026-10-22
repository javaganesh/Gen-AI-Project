interface Props {
  company: string;
  setCompany: (value: string) => void;
  startResearch: () => void;
}

function SearchBar({
  company,
  setCompany,
  startResearch
}: Props) {

  return (
    <div>
      <input
        value={company}
        placeholder="Enter Company Name"
        onChange={(e) =>
          setCompany(e.target.value)
        }
      />

      <button onClick={startResearch}>
        Research
      </button>
    </div>
  );
}

export default SearchBar;