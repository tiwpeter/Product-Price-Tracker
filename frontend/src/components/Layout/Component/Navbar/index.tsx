import historyIcon from "../../../../assets/icons/history.png";

const Navbar = () => {
  return (
    <header className="w-full">
      <nav className="px-20 py-4">
        <div className="flex items-center gap-1">
          <img src={historyIcon} alt="History Icon" />
          <p className="text-xl font-bold">
            Price<span className="text-primary">Wise</span>
          </p>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
