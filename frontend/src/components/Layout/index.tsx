import type { FunctionComponent, ReactNode } from "react";
import Navbar from "./Component/Navbar";

type LayoutProps = {
  children?: ReactNode;
};

const MainLayout: FunctionComponent<LayoutProps> = ({ children }) => {
  return (
    <>
      <Navbar />
      {children}
    </>
  );
};

export default MainLayout;
