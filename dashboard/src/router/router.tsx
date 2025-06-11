import { createBrowserRouter, RouterProvider } from "react-router-dom";

//Pages imports
import Dashboard from "../pages/Dashboard";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard />,
  },
]);

export function Routes() {
  return <RouterProvider router={router} />;
}
