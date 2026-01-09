import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

import ProductsPage from "./features/products/pages/ProductsPage";
import MainLayout from "./components/Layout";

export const router = createBrowserRouter([
  {
    element: <MainLayout />, // 👈 เรียก Layout ตรงนี้
    children: [
      {
        path: "/",
        element: <ProductsPage />,
      },
    ],
  },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
