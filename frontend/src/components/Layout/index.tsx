import type { FunctionComponent } from "react";
import { Outlet } from "react-router-dom";
import Navbar from "./Component/Navbar";

const MainLayout: FunctionComponent = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export default MainLayout;
